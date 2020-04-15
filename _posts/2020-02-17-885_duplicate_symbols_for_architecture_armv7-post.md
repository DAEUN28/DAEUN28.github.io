---
title: "885 duplicate symbols for architecture armv7"
date: 2020-02-17
toc: true
toc_sticky: true
toc_label: "목차"
tags:
  - Swift
  - iOS
categories: "에러일기"
---



### 에러

Realm 라이브러리 빌드에러

```
885 duplicate symbols for architecture armv7
```



### 배경

FirebaseRemoteconfig를 Podfile에 추가하고 pod install한 후, 코드 빌드 하는 도중 에러가 발생했다.



### 해결

간단하다. 팟 초기화,,, 아무래도 팟이 꼬여서 생긴 문제 같다. 

```
pod deintegrate
pod install
```



### 링크

[https://stackoverflow.com/questions/26303782/duplicate-symbols-for-architecture-arm64/39605771](https://stackoverflow.com/questions/26303782/duplicate-symbols-for-architecture-arm64/39605771)

