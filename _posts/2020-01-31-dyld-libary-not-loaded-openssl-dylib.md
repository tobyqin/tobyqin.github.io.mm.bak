---
title: "Library not loaded: /usr/local/opt/openssl@1.1/lib/libcrypto.1.1.dylib"
categories: [Tech]
tags: [openssl,ssh,git]
date: 2020-01-31
---

因为升级了MacOSX和openssl，然后Jekyll和Python都坏了，报各种错误。

<!-- more -->

## 问题描述

Python和Git都会报错。

> dyld: Library not loaded: /usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/Python
>   Referenced from: /Users/tobyqin/src/service/venv/bin/python
>   Reason: image not found
>
> dyld: Library not loaded: /usr/local/opt/openssl@1.1/lib/libcrypto.1.1.dylib 
> Referenced from: /usr/local/bin/ssh 
> Reason: image not found 
> fatal: Could not read from remote repository. 

网上查了各种方案，头疼了好久。

## 解决方案

**卸载新版的openssl，然后安装没有问题的openssl，python和jekyll就好了。**

```shell
brew update && brew upgrade
brew uninstall --ignore-dependencies openssl
brew install https://github.com/tebelorg/Tump/releases/download/v1.0.0/openssl.rb
```

但是，git和ssh却坏了。

**重新或者强制安装最新的openssh就好了**。

```shell
$ brew reinstall openssh
```

这时后python又坏了，因为它和openssh依赖的openssl版本不一致。

这时候需要切换默认的openssl版本，就可以解决所有问题。

```shell
$ brew switch openssl 1.0.2t
Cleaning /usr/local/Cellar/openssl/1.0.2t
Opt link created for /usr/local/Cellar/openssl/1.0.2t
```

