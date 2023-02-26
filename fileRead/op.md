# 文件操作

## open

`open(name,mode,encoding)`

以对应模式打开对应路径名称的文件

```python
f = open("python.txt","r",encoding="UTF-8")
```

注：`encoding`不在第三位，必须使用关键字传参

## read

`read(byte)`

从对应的文件对象中读取相应字节的内容并返回

```python
inner = f.read(10)
```

## readlines

`readlines()`

读取文件全部内容，并且按照行分元素储存在列表中

```python
lines = f.readlines()
```

## readline

`readline()`

读取一行数据，以 str 的方式储存

```python
line = f.readline()
```

## close

`close()`

关闭文件

```python
f.close()
```

## with open

`with open as `

仅在局部打开文件，并在离开域时自动关闭

```python
with open("python.txt","r",encoding="UTF-8") as f:
	print(f.read());
```

## write

`write(str)`

将字符串写入缓存去的文件中

```python
f.write(str)
```

## flush

`flush`

将缓存区的文件更新到硬盘中

```python
f.flush()
```

