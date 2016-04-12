---
layout: post
title: Git通过代理访问Github
category: Document
tags: git github
year: 2012
month: 05
day: 13
published: true
summary: 公司代理如何拥抱github，使用ssh协议代理喽
image: pirates.svg
comment: true
---

网络代理下，用 git 通过 ssh 协议与 github 仓库对接，就是不好用，因为：

1. https
2. ssh

解决方法：

__ssh协议代理__

前提准备：

- git
- ssh

步骤如下：

1. 配置.ssh/config:

```
$ vi ~/.ssh/config
```

写下如下配置项：

```
Host github.com
Hostname ssh.github.com
Port 443
ProxyCommand ~/.ssh/ssh-https-tunnel %h %p
```

2. 下载ssh-https-tunel，可从http://zwitterion.org/software/ssh-https-tunnel/ssh-https-tunnel下载，保存到~/.ssh下，添加可执行权限。

3. 修改host，port，user，pass：

```
# Proxy details
my $host = "proxy.xxx.com";
my $port = 8000;

# Basic Proxy Authentication - leave empty if you don't need it
my $user = "usr";
my $pass = "passwd";

```

4. 用git 对接你的github仓库吧：

```
$ git clone git@github.com:fooyou/jekyll-bootstrap.git
```

## 其他

也可使用 haproxy
