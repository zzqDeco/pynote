# list学习笔记

## 简述

list 是 python 支持的可变长数组，与 cpp 的 vector 类似。可以做到均摊优秀的末端插入删除，以及任意下标访问操作。尽管支持```insert(i,element)```和```pop(i)```的操作，但实际上的底层是暴力重构，复杂度很高。list有序支持下标访问

## 基本方法支持

### index

```index(element)```，hash 查询某元素的位置，O(1)

### insert

你可以使用```insert(i,element)```在任意位置插入一个元素，插入的元素位于 i 的位置，O(n)

### append

```append(element)```，在末尾追加一个元素，O(1)

### extend

```extend(vector)```，在末尾追加一个容器，依次插入，复杂度取决于另一个容器的类型和大小

### pop

```pop(i)```，删除 i 位置上的元素并返回，O(n)

注：可以用 del 关键字实现同样的效果，但不会返回值

### remove

```remove(element)```，移除第一个匹配的元素（估计原理是链式反应前向星）

### clear

清空 list

### count

```count(element)```，统计元素出现次数

### len（不是内部方法）

```len(vector)```，计算对应容器的 size

### count

```count(element)```，统计某个元素出现次数

## 总结

list 是一个有序可重可修改的混装容器