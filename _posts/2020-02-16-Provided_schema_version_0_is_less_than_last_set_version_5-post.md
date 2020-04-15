---
title: "Provided schema version 0 is less than last set version 5."
date: 2020-02-16
tags:
  - Swift
  - iOS
categories: "에러사전"
---

안녕하세요😃 또 오랜만이네요,,, 그동안 너무 바빠서 글을 못쓰고 있었습니다,,ㅠㅠㅜㅠ 그래도 그동안 진행한 프로젝트에서 배운게 많아서 더 좋은 글들을 쓸 수 있을 것 같아요! 프로젝트를 진행하면서 여러 에러들을 만났어요. 덕분에 해결방법을 찾느라 삽질을 조금 했네요,,, 그래서 앞으로 에러를 만날때마다 기록해두고 시간날때 포스팅을 하려고 합니다☺️ 대부분의 개발자들이 IDE에서 주는 에러메시지로 구글링을 많이 하니까 제목은 항상 에러메시지로 하려고해요! 도움이 되셨으면 좋겠어요🙏



### 에러

```
Fatal error: 'try!' expression unexpectedly raised an error: Error Domain=io.realm Code=1 "Provided schema version 0 is less than last set version 5." UserInfo={NSLocalizedDescription=Provided schema version 0 is less than last set version 5., Error Code=1}
```



### 배경

```swift
optional func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool
```

위 함수에서 Realm의 schema version을 설정하기 전에 Object에 접근했다. 그래서 앱을 새로 빌드하자마자 에러가 발생했다.



### 해결

에러메시지를 보면 schema version이 0인데 0은 Realm의 기본 값이므로 에러가 발생한 Object에 접근한 시점이 configuration 전이라는 것을 알 수 있다. 따라서 앱을 실행하고 가장 처음 접근하는 Object에 접근하기 전에 Realm을 configuration하면 해결된다.



### 링크

[https://github.com/realm/realm-cocoa/issues/2723](https://github.com/realm/realm-cocoa/issues/2723)

