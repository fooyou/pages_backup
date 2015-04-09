---
layout: post
title: pickle和cPickle：Python对象的序列化（上）
category: Coding
tags: python 序列化 多进程
year: 2015
month: 04
day: 09
published: true
summary: pickle模块实现了一种算法，将任意一个Python对象转化成一系列字节（byets）。此过程也调用了serializing对象。代表对象的字节流之后可以被传输或存储，再重构后创建一个拥有相同特征（the same characteristics）的新的对象。 
image: first_post.svg
---

*目的：Python对象序列化*

*可用性：pickle至少1.4版本，cPickle 1.5版本以上*

------

`pickle`模块实现了一种算法，将任意一个Python对象转化成一系列字节（byets）。此过程也调用了`serializing`对象。代表对象的字节流之后可以被传输或存储，再重构后创建一个拥有相同特征（the same characteristics）的新的对象。

`cPickle`使用C而不是Python，实现了相同的算法。这比Python实现要快好几倍，但是它不允许用户从Pickle派生子类。如果子类对你的使用来说无关紧要，那么cPickle是个更好的选择。

*__警告:__ 本文档直接说明，pickle不提供安全保证。如果你在多线程通信（inter-process communication）或者数据存储或存储数据中使用pickle，一定要小心。请勿信任你不能确定为安全的数据。*


## 导入

------

如平常一样，尝试导入cPickle，给它赋予一个别名“pickle”。如果因为某些原因导入失败，退而求其次到Python的原生（native）实现pickle模块。如果cPickle可用，能给你提供一个更快速的执行，否则只能是轻便的执行（the portable implementation）。


```python
try:
   import cPickle as pickle
except:
   import pickle
```


## 编码和解码

------

第一个例子将一种数据结构编码成一个字符串，然后把该字符串打印至控制台。使用一种包含所有原生类型（native types）的数据结构。任何类型的实例都可被腌渍（pickled，译者注：模块名称pickle的中文含义为腌菜），在稍后的例子中会演示。使用pickle.dumps()来创建一个表示该对象值的字符串。


```python
try:
    import cPickle as pickle
except:
    import pickle
import pprint

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'DATA:',
pprint.pprint(data)

data_string = pickle.dumps(data)
print 'PICKLE:', data_string
```

pickle默认仅由ASCII字符组成。也可以使用更高效的二进制格式（binary format），只是因为在打印的时候更易于理解，本页的所有例子都使用ASCII输出。

```
$ python pickle_string.py

DATA:[{'a': 'A', 'b': 2, 'c': 3.0}]
PICKLE: (lp1
(dp2
S'a'
S'A'
sS'c'
F3
sS'b'
I2
sa.
```

## 重构对象的问题

------

当与你自己的类一起工作时，你必须保证类被腌渍出现在读取pickle的进程的命名空间中。只有该实例的数据而不是类定义被腌渍。类名被用于在反腌渍时，找到构造器（constructor）以创建新对象。以此——往一个文件写入一个类的实例为例：

```python
try:
    import cPickle as pickle
except:
    import pickle
import sys

class SimpleObject(object):

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

if __name__ == '__main__':
    data = []
    data.append(SimpleObject('pickle'))
    data.append(SimpleObject('cPickle'))
    data.append(SimpleObject('last'))

    try:
        filename = sys.argv[1]
    except IndexError:
        raise RuntimeError('Please specify a filename as an argument to %s' % sys.argv[0])

    out_s = open(filename, 'wb')
    try:
        # 写入流中
        for o in data:
            print 'WRITING: %s (%s)' % (o.name, o.name_backwards)
            pickle.dump(o, out_s)
    finally:
        out_s.close()
```

在运行时，该脚本创建一个以在命令行指定的参数为名的文件：

```
$ python pickle_dump_to_file_1.py test.dat

WRITING: pickle (elkcip)
WRITING: cPickle (elkciPc)
WRITING: last (tsal)
```

一个在读取结果腌渍对象失败的简化尝试：

```python
try:
    import cPickle as pickle
except:
    import pickle
import pprint
from StringIO import StringIO
import sys


try:
    filename = sys.argv[1]
except IndexError:
    raise RuntimeError('Please specify a filename as an argument to %s' % sys.argv[0])

in_s = open(filename, 'rb')
try:
    # 读取数据
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print 'READ: %s (%s)' % (o.name, o.name_backwards)
finally:
    in_s.close()
```

该版本失败的原因在于没有 SimpleObject 类可用：

```
$ python pickle_load_from_file_1.py test.dat

Traceback (most recent call last):
  File "pickle_load_from_file_1.py", line 52, in <module>
    o = pickle.load(in_s)
AttributeError: 'module' object has no attribute 'SimpleObject'
```

正确的版本从原脚本中导入 SimpleObject ，可成功运行。

添加：

```python
from pickle_dump_to_file_1 import SimpleObject
```

至导入列表的尾部，接着重新运行该脚本：

```
$ python pickle_load_from_file_2.py test.dat

READ: pickle (elkcip)
READ: cPickle (elkciPc)
READ: last (tsal)
```

当腌渍有值的数据类型不能被腌渍时（套接字、文件句柄（file handles）、数据库连接等之类的），有一些特别的考虑。因为使用值而不能被腌渍的类，可以定义 \_\_getstate\_\_() 和 \_\_setstate\_\_() 来返回状态（state）的一个子集，才能被腌渍。新式类（New-style classes）也可以定义\_\_getnewargs\_\_()，该函数应当返回被传递至类内存分配器（the class memory allocator）（C.\_\_new\_\_()）的参数。使用这些新特性的更多细节，包含在标准库文档中。


## 环形引用（Circular References）

------

pickle协议（pickle protocol）自动处理对象间的环形引用，因此，即使是很复杂的对象，你也不用特别为此做什么。考虑下面这个图：