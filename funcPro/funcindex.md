# 函数传参数

## 位置参数

```python
def func(a,b,c):
	print(f"{a},{b},{c}")
	
func("my",20,"new")
```

## 关键字参数

key = value

```python
def func(a,b,c):
	print(f"{a},{b},{c}")
	
func(a="my",b=20,c="new")
func(b=20,a="my",c="new")
func(a="my",c="new",b=20)
```

## 不定长参数

```python
def func(*args1):
  print(args1)

func("Tom")

func("Tom",18)

def func(**args2):
  print(args2)

func(name="Tom")

func(name="Tom",age=18)
#单个星号会将不定长参数按照元组存储，双星号表示用key:value的形式用字典存储
```
