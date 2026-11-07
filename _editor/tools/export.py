"""Export public read-only HTML; never copy runtime state or credentials.

Env overrides:
  WIKI_EXPORT_ORIGIN    — editor server URL (default http://127.0.0.1:3333)
  WIKI_EXPORT_PUBLIC    — public origin for canonical/og (default https://daeun28.github.io)
  WIKI_EXPORT_DEST      — output root. The /wiki/ tree goes under this path.
                          Default <repo>/public which keeps old local behavior.
"""
import json, os, re, shutil, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from html import unescape
ROOT=Path(__file__).resolve().parents[1]
ORIGIN=os.environ.get('WIKI_EXPORT_ORIGIN','http://127.0.0.1:3333')
PUBLIC_ORIGIN=os.environ.get('WIKI_EXPORT_PUBLIC','https://daeun28.github.io')
DEST=Path(os.environ.get('WIKI_EXPORT_DEST', str(ROOT/'public'))).resolve()
BASE='/wiki'
PAGE_LIMIT=2000
def fetch(path):
    try:
        with urllib.request.urlopen(ORIGIN+urllib.parse.quote(path,safe='/%?=&'), timeout=20) as r: return r.read().decode()
    except urllib.error.HTTPError as e:
        if e.code==404: return e.read().decode()
        raise
def canon_path(path):
    """Collapse the many URL spellings of one wiki title to a single key.
    Engine treats '_' and ' ' as the same character in titles (AGENTS.md §5),
    so '/wiki/A B' and '/wiki/A_B' resolve to the same page; keep underscore form.
    """
    if not path: return path
    sp=urllib.parse.urlsplit(path)
    p=urllib.parse.unquote(sp.path)
    if p.startswith('/wiki/'):
        p='/wiki/'+p[6:].replace(' ','_')
    return urllib.parse.urlunsplit(('','',urllib.parse.quote(p,safe='/'),sp.query,sp.fragment))
def public_path(path):
    path=canon_path(path)
    sp=urllib.parse.urlsplit(path)
    p=sp.path
    if p=='/': return BASE+'/'
    if p.startswith('/wiki/'): return BASE+'/p/'+p[6:].rstrip('/')+'/'
    return BASE+p.rstrip('/')+'/'
def public_url(path):
    return PUBLIC_ORIGIN+public_path(path)
pages=json.loads(fetch('/api/all'))['pages']
records=[]
for page in pages:
    records.append(json.loads(fetch('/api/wiki/'+urllib.parse.quote(page['title'],safe=''))))
queue=[canon_path(p) for p in (['/','/all','/discover','/search']+['/wiki/'+urllib.parse.quote(p['title'],safe='') for p in pages])]
seen=set()
DEST.parent.mkdir(parents=True,exist_ok=True)
stage=DEST.parent/(DEST.name+'-building')
if stage.exists(): shutil.rmtree(stage)
stage.mkdir(parents=True)
def transform(source):
    # Strip all mutation/account/history links, rather than exposing dead controls.
    source=re.sub(r'<li>\s*<a\b[^>]*href="[^"]*(?:/login|/logout|/new|/settings|/account|/register)[^"]*"[^>]*>.*?</a>\s*</li>','',source,flags=re.S)
    source=re.sub(r'<a\b[^>]*href="[^"]*(?:/edit|/history|/login|/logout|/new|/settings|/account|/register)(?:[/?"][^>]*)?>.*?</a>','',source,flags=re.S)
    source=re.sub(r'<link[^>]+rel="alternate"[^>]*>','',source)
    source=re.sub(r'<meta[^>]+name="csrf[^>]*>','',source)
    def attr(m):
        key,raw=m.groups(); value=unescape(raw); u=urllib.parse.urlsplit(value)
        if u.scheme and u.netloc!='127.0.0.1:3333': return m.group()
        path=u.path
        if not path.startswith('/'): return m.group()
        if path.startswith('/wikiwikiwiki/assets/'): target=BASE+path
        elif path.endswith(('.txt','.md')):
            target=BASE+'/sources/'+urllib.parse.quote(urllib.parse.unquote(path[6:]).replace('_',' '),safe='')
        elif path=='/random': target=BASE+'/random/'
        elif path in ['/','/all','/discover','/search'] or path.startswith(('/wiki/','/tags/')):
            if u.query: return key+'="'+BASE+'/all/"'
            canon=canon_path(path)
            if canon not in seen and canon not in queue: queue.append(canon)
            target=public_path(path)
        else: return key+'="'+BASE+'/"'
        if u.fragment: target+='#'+u.fragment
        return key+'="'+target+'"'
    source=re.sub(r'(href|src|action)="([^"]*)"',attr,source)
    def rewrite_origin(m):
        rest=m.group()[len(ORIGIN):]
        u=urllib.parse.urlsplit(rest); p=u.path or '/'
        pdec=urllib.parse.unquote(p)
        if pdec.startswith('/wikiwikiwiki/assets/'): mapped=BASE+p
        elif pdec=='/random': mapped=BASE+'/random/'
        elif pdec.startswith('/wiki/') or pdec in ['/','/all','/discover','/search']: mapped=public_path(p)
        else: mapped=BASE+'/'
        out=PUBLIC_ORIGIN+mapped
        if u.query: out+='?'+u.query
        if u.fragment: out+='#'+u.fragment
        return out
    source=re.sub(r'http://127\.0\.0\.1:3333[^"\'<>\s]*',rewrite_origin,source)
    source=re.sub(r'(<link[^>]+rel="canonical"[^>]*href=")(/[^"]*)(")',lambda m:m.group(1)+PUBLIC_ORIGIN+m.group(2)+m.group(3),source)
    return source.replace('</body>','<script src="/wiki/static.js"></script></body>')
while queue:
    path=queue.pop(0)
    path=canon_path(path)
    if path in seen: continue
    if len(seen)>PAGE_LIMIT: raise RuntimeError('Export exceeded prototype page limit')
    seen.add(path)
    source=transform(fetch(path))
    target=stage/urllib.parse.unquote(public_path(path)).lstrip('/')/'index.html'
    target.parent.mkdir(parents=True,exist_ok=True);target.write_text(source)
assets=stage/'wiki/wikiwikiwiki/assets'
engine_assets=ROOT/'editor/wikiwikiwiki/assets' if (ROOT/'editor/wikiwikiwiki/assets').is_dir() else ROOT/'wikiwikiwiki/assets'
shutil.copytree(engine_assets,assets)
# User-uploaded images live in _editor/user-images/ (committed by the Vercel
# editor via GitHub Contents API) and get served at /wiki/images/<file>.
user_images=ROOT/'user-images'
if user_images.is_dir():
    shutil.copytree(user_images, stage/'wiki/images')
(stage/'wiki/data.json').write_text(json.dumps(records,ensure_ascii=False))
for p in records:
    target=stage/'wiki/sources'/(p['title']+'.txt')
    target.parent.mkdir(parents=True,exist_ok=True);target.write_text(p['content'])
random_dir=stage/'wiki/random';random_dir.mkdir()
(random_dir/'index.html').write_text('<meta charset="utf-8"><script src="/wiki/static.js"></script>')
(stage/'wiki/static.js').write_text("""
(async()=>{
 const data=await fetch('/wiki/data.json').then(r=>r.json());
 const link=p=>'/wiki/p/'+encodeURIComponent(p.title.replace(/ /g,'_'))+'/';
 if(location.pathname==='/wiki/random/' && data.length) {location.replace(link(data[Math.floor(Math.random()*data.length)]));return;}
 if(location.pathname!='/wiki/search/')return;
 const form=document.querySelector('form[role=search]');if(!form)return;
 const result=document.createElement('div');result.className='content';result.setAttribute('aria-live','polite');form.after(result);
 const run=()=>{
   const q=form.querySelector('[name=q]').value.trim().toLowerCase();
   result.replaceChildren();
   if(!q)return;
   const scope=form.querySelector('[name=scope]').value;
   const haystack=p=>scope==='title'?p.title:scope==='content'?p.content:p.title+' '+p.content;
   const hits=data.filter(p=>haystack(p).toLowerCase().includes(q));
   const ul=document.createElement('ul');
   hits.forEach(p=>{const li=document.createElement('li'),a=document.createElement('a');a.href=link(p);a.textContent=p.title;li.append(a);ul.append(li)});
   result.append(hits.length?ul:document.createTextNode('검색 결과가 없습니다.'));
 };
 form.addEventListener('submit',e=>{e.preventDefault();run()});
 const params=new URLSearchParams(location.search);
 const scopeParam=params.get('scope');if(scopeParam){const sel=form.querySelector('[name=scope]');if([...sel.options].some(o=>o.value===scopeParam))sel.value=scopeParam;}
 const q=params.get('q');if(q){form.querySelector('[name=q]').value=q;run();}
})().catch(console.error);
""")
# Keep the package intentionally limited to public files.
license_src=ROOT/'editor/LICENSE' if (ROOT/'editor/LICENSE').is_file() else ROOT/'LICENSE'
shutil.copy(license_src,stage/'wiki/LICENSE.txt')
if DEST.exists(): shutil.rmtree(DEST)
stage.rename(DEST)
print(f'Exported {len(records)} documents, {len(seen)} views to {DEST}')
