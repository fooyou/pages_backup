---
layout: post
title: Ubuntu上编译ffmpeg的动态链接库（.so）
category: Coding
tags: ffmpeg ubuntu
year: 2015
month: 04
day: 08
published: true
summary: ubutnu中使用动态链接库的场景 
image: first_post.svg
---

**问题**

*从[ffmpeg官网](https://ffmpeg.org/)上下载了源码，然后按照其[编译文档](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu)在ubuntu(12.04~14.04)上进行编译，然后发现生成的链接库里没有动态库.so文件。如何生成动态链接库呢？*

**解决步骤**

1. configure时选项要使用 `--enable-shared` 来打开动态链接库选项。
2. configure时，prefix默认为/usr/local，然而该目录默认情况下是不在ldconfig下的，所以要添加一下方法如下：

    ```sh
    sudo vi /etc/ld.so.conf.d/libc.conf
    ```

    然后添加如下路径就可以了（PS：14.04上在创建该文件时就自动写好了）

    ```sh
    /usr/local/lib
    ```

    然后应用该配置：

    ```sh
    sudo ldconfig -v
    ```

3. 在源码目录下，就可以build了：

    ```sh
    ./configure --enable-shared && make && make install
    ```
    
<div class="row">   
    <div class="span9 columns">    
        <h2>评论</h2>
        <p>欢迎回复，请保证一不跑题二要干净</p>
        <div id="disqus_thread"></div>
        <script type="text/javascript">
            /* * * CONFIGURATION VARIABLES * * */
            var disqus_shortname = 'meshinestar';
            
            /* * * DON'T EDIT BELOW THIS LINE * * */
            (function() {
                var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
                (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
            })();
        </script>
        <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
    </div>
</div>
