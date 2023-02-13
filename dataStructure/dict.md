# dict 笔记

## 简述

dict 就是 map ，以 key : value 的形式结合为元素，平衡树类型的数据结构，虽然有序，但顺序很多时候为 hash 值，所以等于无序的结构

## 常用方法支持

### []

支持用 [] 解析 key 得到 value

### clear

清空容器

### pop

pop(key)，取出一个元素，并删除

### keys

取得容器中所有 key 值

### len（不是内部方法）

```len(vector)```，计算对应容器的 size

## 总结

```python
for key in dict1:
	print(f"the {key}\'s value in dict is: {dict1[key]}")
```



