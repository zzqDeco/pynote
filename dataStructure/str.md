# str学习笔记

## 简述

某种意义上就是特殊的元组，python的str是不支持修改的，所以各种操作的结果都是以返回值的方式呈现的

## 常用方法支持

### index

```index(str)```，查询某字符串在母串的位置

### replace

```replace(str,str)```，将母串中匹配的子串替换为另一个字符串

### split

```split(str)```，将母串按照子串切分得到子串列表

### strip

```strip(str)```，除去前后所有的 str 中含有的字符，若无参则自动删除空白字符

### count

```count(element)```，统计某个元素出现次数

### len（不是内部方法）

```len(vector)```，计算对应容器的 size

## 总结

str 是特殊的元组
