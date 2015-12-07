---
layout: post
title: 在elementary os中修改终端字体
category: Document
tags: linux
date: 2015-12-07 14:12:52
published: true
summary: 看手机玩Pad眼睛受伤啊，这不又近视了，必须调大终端字体才能看清楚了。
image: pirates.svg
comment: true
---

## 方法一：安装 dconf-editor

```
$ sudo apt-get install dconf-tools
```

安装完成后打开App， 找到 org-> gnome -> desktop -> interface -> monospace-font-name 双击后按下面的语法输入 \[font-name\]\[property\]\[size\]，比如：`Droid Sans Mono 12`。

这里设置的是系统通用等宽字体的地方，终端等地方的字体默认就取自这里。

还可以只针对终端设置字体类型：org -> pantheon -> terminal -> settings -> font 输入要设置的值语法同上。


## 方法二：使用 gsettings 命令设置

```
$ gsettings set org.gnome.desktop.interface monospace-font-name 'Droid Sans Mono 12'
```

或者：

```
$ gsettings set org.pantheon.terminal.settings font 'Droid Sans Mono 12'
```

当然其他的选项也可以通过这种方式设置。

参考：

> http://elementaryos.stackexchange.com/questions/1149/how-can-i-chage-the-default-font/1153#1153

