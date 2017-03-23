---
layout: post
title: Aho-Corasick 算法
category: Document
tags: algorithm 
date: 2017-03-22 10:03:01
published: true
summary: 
image: pirates.svg
comment: true
---

简介

Aho-Corasick算法简称AC算法，通过将模式串预处理为确定有限状态自动机，扫描文本一遍就能结束。其复杂度为O(n)，即与模式串的数量和长度无关。


**思想**

自动机按照文本字符顺序，接受字符，并发生状态转移。这些状态缓存了“按照字符转移成功（但不是模式串的结尾）”、“按照字符转移成功（是模式串的结尾）”、“按照字符转移失败”三种情况下的跳转与输出情况，因而降低了复杂度。


**基本构造**

AC 算法中有三个核心函数，分别是：

- success: 成功转移到另一个状态（也称 goto 表或者 success 表）
- failure: 不可顺着字符串跳转的话，则跳转到一个特定的节点（也称 failure 表），从根节点到这个特定的节点的路径恰好是失败前的文本的一部分。
- emits: 命中一个模式串（也称 output 表）


**举例**

以经典的 ushers 为例，模式串是 he/ she/ his/ hers，文本为 "ushers"。构建的自动机如图：

![自动机构件图](https://g.gravizo.com/svg?
digraph G {
    rankdir=LR;
    node [shape="circle"];
    {
        0 -> 0 [label="!{h,s}"];
        0 -> 1 [label="h"];
        0 -> 3 [label="s"];
        1 -> 2 [label="e"];
        1 -> 6 [label="i"];
        2 -> 8 [label="r"];
        8 -> 9 [label="s"];
        3 -> 4 [label="h"];
        4 -> 5 [label="e"];
        6 -> 7 [label="s"];
        1 -> 0 [style=dotted];
        2 -> 0 [style=dotted, label="{he}"];
        3 -> 0 [style=dotted];
        6 -> 0 [style=dotted];
        8 -> 0 [style=dotted];
        4 -> 1 [style=dotted];
        5 -> 2 [style=dotted, label="{he, she}"];
        7 -> 3 [style=dotted, label="{his}"];
        9 -> 3 [style=dotted, label="{hers}"];
    };
    {rank = same; 1; 3;};
    {rank = same; 2; 6; 4;};
    {rank = same; 8; 7; 5;};
}
)
