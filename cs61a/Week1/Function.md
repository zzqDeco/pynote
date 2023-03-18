# Function

## Algorithm

A precise sequence of simple steps to solve a problem

## Python

translating an algorithm into a computer program

基本的 python 操作教学

注意的是 python 比其他语言更进一步的将函数也看作一个对象，你同样可以把函数在很多地方当作变量来操作

同时 python 的 division 是 `/`，int division 是 `//`，exponentiation 有三种形式

```python
a**b
pow(a,b) # 前两个方式基本相同
pow(a,b,c) # 后面的这个的意思是计算a^b%c的结果
```

同时 python 支持一个逆天的双返回

```python
def return_two_things:
	return (x+y,x*y)
	
(s,p) = return_two_things(2,5)
```

