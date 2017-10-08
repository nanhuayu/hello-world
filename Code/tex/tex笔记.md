# 大文档拆分
当处理很大的文档文件时,有时找们希望将文件分成若干部分。

* include

\include{filename} 在文挡区我们可以使用这条命令插入另一个文件的内容，LATEX 在处理插入的文本以前将启动新的一个页面。

* includeonly

\includeonly{filename1,filename2,...} 这条命令可在导言部分使用,允许LATEX 对可插入的文本文件进行限制:这条命令执行后，上面的\include{filename}命令中的 filename 叁数必须是 \includeonly{filename1,filename2,...}命令叁数中的一个。 注意文件名 filename1,filename2,... 同其后面的逗号之间不能有空格。

* input

\input{filename} \include 命令将在新的页面上对插人的文件文本迸行徘版,如果你不希望这样,可以用上面的命令插入别的文件。 

参见: [Latex中大文件的拆分与管理](http://www.eetop.cn/blog/html/03/6503-33399.html)


# 怎样将几个TEX文档合并成一个
```
把每个文档的\begin{document}之前的东西删了，再把\end{document}删了
建一个新文档，只有\begin{document}之前的东西，和\end{document}。
在新建的那个文档的\begin{document}和\end{document}之间加：
\include{文件名1}
\include{文件名2}
。。。。
可以不要后缀。
BAIDU一个：“LATEX 多文档”或者“latex \include”
用\input {file} 也行，这个命令与\include的区别是：前者不开新页，后者开新页
```
参见: [怎样将几个TEX文档合并成一个](http://bbs.ctex.org/forum.php?mod=viewthread&tid=48737)

# 

如何使得各章既可以被包含在另一个文件中也可以独立编译呢？   
方法是将main.tex和chap1.tex作如下修改：

% main.tex
\documentclass{book}
\def\allfiles{}
\begin{document}
\title{A LaTeX Book}
\author{cohomo@blogbus}
\date{}maketitle
\input{chap1}
\input{chap2}
\end{document}

% chap1.tex 
\ifx\allfiles\undefined
\documentclass{article}
\begin{document}
\title{Something in Title}
\author{cohomo@blogbus}
\date{}
\maketitle
\else
\chapter{Chap1's Title}
\fi
\section{First Section}
\section{Second Section}
\ifx\allfiles\undefined
\end{document}
\fi

这样编写长文档就很方便和灵活了。

参见: [Latex之文件拆分及独立编译](http://blog.sina.com.cn/s/blog_59cf67260101eat1.html)
