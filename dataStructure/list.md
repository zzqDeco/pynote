# list学习笔记

## 简述

list 是 python 支持的可变长数组，与 cpp 的 vector 类似。可以做到均摊优秀的末端插入删除，以及任意下标访问操作。尽管支持```insert(i,element)```和```pop(i)```的操作，但实际上的底层是暴力重构，复杂度很高

## 基本方法支持

### index

```index(element)```，hash 查询某元素的位置，O(1)

### insert

你可以使用```insert(i,element)```在任意位置插入一个元素，插入的元素位于 i 的位置，O(n)

### append

```append(element)```，在末尾追加一个元素,O(1)