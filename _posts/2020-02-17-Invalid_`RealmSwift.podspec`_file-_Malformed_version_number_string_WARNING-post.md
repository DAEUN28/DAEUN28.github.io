---
title: "[에러] Invalid `RealmSwift.podspec` file: Malformed version number string WARNING"
date: 2020-02-17
toc: true
toc_sticky: true
toc_label: "목차"
tags:
  - Cocoapods
  - 터미널
categories: "에러일기"
---



### 에러

터미널 에러

```
Analyzing dependencies
Pre-downloading: `DKPhotoGallery` from `https://github.com/zhangao0086/DKPhotoGallery`, commit `f7eac2412b53689598799de55237eef65ccc35e2`
Pre-downloading: `Realm` from `https://github.com/realm/realm-cocoa.git`, commit `9011b2df17019552d7acae3ed085bf8c01a6a38f`, submodules `true`
[!] Failed to load 'Realm' podspec: 
[!] Invalid `RealmSwift.podspec` file: Malformed version number string WARNING: The active Xcode command line tools, as returned by 'xcode-select -p', are not from Xcode.
         The newest version of Xcode will be used instead.
4.3.1.

 #  from /var/folders/4h/4cr354890tg43f11tj07py3w0000gn/T/d20200214-15896-kfv3fo/RealmSwift.podspec:12
 #  -------------------------------------------
 #    s.homepage                  = "https://realm.io"
 >    s.source                    = { :git => 'https://github.com/realm/realm-cocoa.git', :tag => "v#{s.version}", :submodules => true }
 #    s.author                    = { 'Realm' => 'help@realm.io' }
 #  -------------------------------------------


[!] Smart quotes were detected and ignored in your Podfile. To avoid issues in the future, you should not use TextEdit for editing it. If you are not using TextEdit, you should turn off smart quotes in your editor of choice.
```



### 배경

맥을 초기화하고 원래 진행하고 있던 프로젝트를 gitlab에서 clone받은 후 터미널에서 `pod install` 명령어를 실행했다.



### 해결

Xcode -> Preference -> Locations -> Command Line Tools

위 경로의 항목이 제대로 선택되었는지 확인하고 Xcode의 최신버전으로 선택한다.

터미널에서 다음 명령어를 실행한다.

```
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```



### 링크

[https://stackoverflow.com/questions/48959135/pod-install-realm-3-1-1-failed](https://stackoverflow.com/questions/48959135/pod-install-realm-3-1-1-failed)