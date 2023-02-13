# 匿名函数

## 函数作为参数

```python
def test_func(counter):
	print(counter(1, 2))
	
def compute(x, y)
	return x + y;

test_func(compute)
```

## 匿名函数

```python
lambda x, y: x + y
```

临时使用的函数，只能写在一行

```python
def test_func(counter):
	print(counter(1, 2))

test_func(lambda x, y: x + y)
```

