---
title: "삽질안하고 간단하게 Github블로그 개설하기"
date: 2019-11-14
tags:
  - Github블로그
categories: "Github_블로그_튜토리얼"
---



안녕하세요😀 오늘은 Github블로그 정말정말 쉽게 만드는 방법을 알려드릴게요!

제가 이 블로그를 만들면서 처음에는 글을 올릴 목적만 생각해서 공개되어있는 지킬테마에서 몇 개의 파일만 사용했어요. 그런데 이렇게 만드니까 제 마음대로 폰트사이즈를 조정할 수 없더라구요ㅠㅠㅠㅠ 그래서 폰트사이즈를 줄이고 말겠다는 일념으로 삽질을 시작하고 성공했습니다!! 엄청엄청 쉬우니까 꼭 따라해보세용

이 글은 지킬을 굳이 설치하지 않고 경험을 토대로 초보자를 위해 쉽게 변형하여 어려운 개념을 설명하지 않습니다. 그래서 테스트 배포도 설명하지 않아요. 어려운 개념을 원하신다면 다른 글을 추천합니다!



[TOC]





## 1. 테마를 포크해 레포지토리 생성하기

저는 깃허브에서 가장 스타가 많은 [minimal-mistakes](https://github.com/mmistakes/minimal-mistakes)라는 테마를 기준으로 설명드리겠지만 방법은 다 비슷합니다!

>만약 다른 테마를 원하신다면 http://jekyllthemes.org 사이트에서 다양한 테마를 적용할 수 있습니다.



- 먼저 해당 테마의 깃허브 레포지토리에 접속해 포크해줍니다.

  ![](https://user-images.githubusercontent.com/45457678/68925224-eb8c1780-07c5-11ea-92a2-2df5227a69d8.png)



- 포크한 자신의 저장소의 이름을 `깃허브닉네임.github.io`로 변경해줍니다.

  ![](https://user-images.githubusercontent.com/45457678/68925893-86d1bc80-07c7-11ea-9ae6-f91f529812bb.png)



## 2. 필요없는 파일 삭제하기

저는 테마를 변형할 생각은 없어서 필요없는 파일들을 삭제했는데 삭제한 파일들은 다음과 같아요!! 사실 [이 글](https://dreamgonfly.github.io/2018/01/27/jekyll-remote-theme.html)을 보시면 _config.yml, index.html, _post디렉토리만 있어도 동작하기는 합니당 하지만 저의 목적은 `폰트크기조정`이었기 때문에 나중에 혹시 사용할지도 모르는 파일만 남기고 다 삭제했어요. 파일을 삭제하는건 선택입니다! 

삭제한 파일들은 다음과 같습니다.

- 삭제한 디렉토리
  - .github
  - docs
  - test
- 삭제한 파일
  - .editorconfig
  - .gitattributes
  - CHANGELOG.md
  - Gemfile
  - README.md
  - Rakefile
  - banner.js
  - minimal-mistakes-jekyll.gemspec
  - package-lock.json
  - package.json
  - screenshot-layouts.png
  - screenshot.png



## 3. 디렉토리 추가하기

이제 불필요한 파일도 삭제했으니 블로그 글을 담는 디렉토리를 만들어봅시다! 블로그 글을 담는 디렉토리의 이름은 `_post`로 해주세요. 앞으로 작성하는 블로그의 포스트들은 모두 여기에 포함시키면 됩니다.



## 4. _config.yml 파일 수정하기

지금 _config.yml 파일에는 아마 기본값이 들어있을거에요! 이 파일에는 사이트 설정과 관련된 여러가지 속성이 있어요. 원하는 값을 설정하시면 되는데요. 가장 중요한 속성들만 알려드릴게요! 다른 속성들은 재량껏 설정하시면 됩니다. 

제 블로그를 보고 원하는 값을 설정해보세요!!

```yml
locale                   : "ko-KR"
title                    : "DAEUN28"
title_separator          : "-"
subtitle                 : "Swift, iOS, FUN😃"
name                     : "DAEUN28"
description              : "아주 놀라운 작은 개발자의 블로그"
url                      : "https://DAEUN28.github.io"
repository               : "DAEUN28/DAEUN28.github.io"
```

![](https://user-images.githubusercontent.com/45457678/68927699-b1257900-07cb-11ea-991a-89a37840aae7.png)



## 5. 글 작성하기

- `_post` 디렉토리에 `yyyy-mm-dd-title-post.md`라는 파일을 생성합니다. 

  - 네이밍 규칙이 정해져있지는 않습니다! 하지만 일반적으로 이 형식으로 파일 네이밍을 한다고 합니다.

- 블로그 내용의 맨 처음에는 다음과 같이 글의 제목과 날짜, 카테고리, 태그등을 적어줍니다. 이 형식은 [Front Matter](https://jekyllrb.com/docs/front-matter/)라고 불린다고 합니다.

  ```yaml
  title: "삽질안하고 간단하게 Github블로그 개설하기"
  date: 2019-11-14
  tags:
    - Github블로그
  categories: "Github_블로그_튜토리얼"
  ```

- Front Matter뒤에는 어떤 내용을 쓰던 상관없습니다. 다음은 이 글의 시작이에요!!

  ![](https://user-images.githubusercontent.com/45457678/68928703-1aa68700-07ce-11ea-8f40-0a33e1d75c9e.png)



이 튜토리얼은 폰트크기 조정, 카테고리, 태그 페이지 추가 등 계속됩니당🥰

참고 : [https://dreamgonfly.github.io/2018/01/27/jekyll-remote-theme.html](https://dreamgonfly.github.io/2018/01/27/jekyll-remote-theme.html)