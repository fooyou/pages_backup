---
layout: post
title: Solr 5.3.1 linux搭建
category: Document
tags: solr
date: 2015-10-20 15:10:58
published: true
summary: 以前搭建了Solr4.8和4.9，现在都5.3了，重新搭建一下吧，尽管和以前没什么差别，但谁让以前的记录全丢了，只能根据记忆重来一遍了。
image: pirates.svg
comment: true
latex: false
---

## 准备

[官网](http://lucene.apache.org/solr/)下载[Solr 5.3.1源码](http://www.apache.org/dyn/closer.lua/lucene/solr/5.3.1)，（因为源码最小37M，很快下完），加上我有编译它需要的ant环境，不过若有代理的话还得费点功夫。

不过若网速够快，直接下载编译好的压缩包即可，129M，下面就略编译过程了，从配置开始说起。

## 安装Tomcat
