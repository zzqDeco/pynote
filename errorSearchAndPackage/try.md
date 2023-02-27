## 异常捕获

```python
try:
	...
except:
	...
```

尝试执行，若出现异常更换操作方式

```python
try:
	f = open("...","r",encoding="UTF-8")
except:
	f = open("...","w",encoding="UTF-8")
```

或者

```python
try:
	f = open("...","r",encoding="UTF-8")
except Exception:
	f = open("...","w",encoding="UTF-8")
```

可以通过异常变量控制异常的捕获范围,还可以用 else 和 finally 附加内容

```python
try:
	print(a/b)
except (NameError,ZeroDivisionError) as e:
	print("ERROR:"+e)
else:
  print("no error")
finally:
  f.close()
```

try catch 具有传递性