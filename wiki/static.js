
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
