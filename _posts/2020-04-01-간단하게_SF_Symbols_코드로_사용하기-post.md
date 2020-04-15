---
title: "간단하게 SF Symbols 코드로 사용하기"
date: 2020-04-01
tags:
  - iOS
  - Swift
categories: "iOS사용법"
---

안녕하세요 😀

오늘은 에러를 해결한 기념으로 SF Symbols를 코드로 사용하는 방법에 대해서 알아볼게요! 엄청아주많이 간단하답니다~~

SF Symbols는 **iOS 13, watchOS 6, tvOS 13**부터 앱에서 사용 할 수 있는 1500여 가지의 symbol set을 제공합니다. 이제 디자이너없는 프로젝트할 때 아이콘때문에 귀찮은 일은 없을거에요🥰 

먼저 [링크](https://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview/)에서 SF symbols앱을 다운로드해주세요. (**카탈리나** 가 아니라면 다운로드가 불가합니다ㅜ) 다운로드 후 실행하면 다양한 symbol set을 볼 수 있습니다! 

![](https://user-images.githubusercontent.com/45457678/78149719-44a4d100-7471-11ea-8782-a4f864e3ca28.png)

여기서 사용하고자 하는 symbol을 선택하고 `shift + command + c` 를 누르면 symbol 이름을 복사할 수 있습니다! (그냥 `command + c`키는 symbol 자체를 복사하는 단축키에요😊)

이제 UIImage의 이니셜라이저 중 아래의 이니셜라이저의 systemName인자에 붙여넣기 하시면 됩니다!

<script src="https://gist.github.com/DAEUN28/be8cfdac4afa3eeb0ab6885af5e63b4f.js"></script>



아래 예제와 같이 사용해주시면 됩니다😇

<script src="https://gist.github.com/DAEUN28/395da96f896d074ede8751e12e83036c.js"></script>



SymbolConfiguration을 생성해 configuration에 넣어주시면 pointSize, weight, scale등을 커스텀하실 수 있어요.



만약 SF Symbols를 자주 이용한다!!라면 아래와 같이 사용하시면 편하겠죠???

<script src="https://gist.github.com/DAEUN28/7e0ba99a3a4e873cd2a52097b594d26e.js"></script>



오늘도 도움이 되셨다면 좋겠습니다! 잘못된 내용이 있다면 댓글로 알려주세요🤗