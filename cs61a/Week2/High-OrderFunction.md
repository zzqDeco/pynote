# High-OrderFunction

我们已经知道，函数是一种抽象方法，它独立于我们实际的参数，抽象出一种方法论

为了进一步加强抽象，我们需要构造可以接受其他函数作为参数或者返回函数作为返回值的函数。对函数进行操作的函数称为高阶函数（High-order Function），高阶函数作为一种更强大的抽象机制，将极大的增强我们的语言表达能力。对于高阶函数，我们开始看到一种更强大的抽象：一些函数表示一般的计算方法，独立于它们调用的特定函数。

cs61a把人当傻子一样教，让我不想写这部分内容了，感觉自己查文档更好。

唯一要提到的点在于Functions as Returned Values

一个明显的例子是这样的

```python
def compose1(f, g):
	def h(x):
  	return f(g(x))
  return h
```

我们可以使用高阶函数将一个带有多个参数的函数转换为一个带有单个参数的函数链。更具体地说，给定一个函数f(x, y)，我们可以定义一个函数g，使得g(x)(y)等价于f(x, y)。这里，g是一个高阶函数，它接受一个参数x，并返回另一个接受一个参数y的函数。这种变换称为curry

这种变换的显著用法是

```python
>>> def curry2(f):
        """Return a curried version of the given two-argument function."""
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g
>>> def uncurry2(g):
        """Return a two-argument version of the given curried function."""
        def f(x, y):
            return g(x)(y)
        return f
```

Lambda Expressions

The result of a lambda expression is called a lambda function. It has no intrinsic name (and so Python prints `<lambda>` for the name), but otherwise it behaves like any other function.

```python
s = lambda x: x * x
```

我们之前提到过每个函数与变量一样，有着外部链接的名字以及一个内部的名字，而对于lambda函数，他将不具有确定的名字，这样的函数只有一个地址将其标记，他的名称将会被``<lambda>``标记

在此我们发现，函数的地位在python中和变量别无二致，他们都属于first-class element：

1. They may be bound to names.
2. They may be passed as arguments to functions.
3. They may be returned as the results of functions.
4. They may be included in data structures.

这使得在python中函数的表达地位是极大的，与之相反的一个例子便是c语言（但是现在的c语言标准如何我并不太了解，但是c98确实给予函数的地位并不大）

但是我并不认为一个过于抽象的工具是好用的，比如python在此基础上更进一步，提供了一个东西叫做Function Decorators

```python
>>> def trace(fn):
        def wrapped(x):
            print('-> ', fn, '(', x, ')')
            return fn(x)
        return wrapped
>>> @trace
    def triple(x):
        return 3 * x
>>> triple(12)
->  <function triple at 0x102a39848> ( 12 )
```

上面这样的东西等价于

```python
>>> def triple(x):
        return 3 * x
>>> triple = trace(triple)
```

这样的标识符让我们很容易定义一个高阶的函数

但是这样也有明显的坏处，这样写出来的代码的可读性真的无法恭维，其他人阅读你的代码的门槛将会极高，这不太符合我们对抽象的一部分需求。我们想要通过抽象使得问题更加易于理解而不是减少代码量，但是在这里，我们用抽象更像是在减少代码量而不是为了易于理解，别人想要理解这个函数就必须知道相关的一切函数。

但是这也不代表这样是错误的，当我们想要为某些函数统一在之前添加一个功能的时候，这样会很方便

