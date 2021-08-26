Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [1,2,4,5,7,2]
>>> import functools
>>> def add(a,b):
	return a + b

>>> functools.reduce(add, x)
21
>>> import operator
>>> functools.reduce(operator.add, x)
21
>>> functools.reduce(operator.sub, x)
-19
>>> functools.reduce(operator.mul, x)
560
>>> lambda x,y : x + y
<function <lambda> at 0x000001A9FE56CE50>
>>> add
<function add at 0x000001A9FE509040>
>>> (lambda x,y : x + y)(4,5)
9
>>> list(filter(lambda x : x % 2 == 0, [4,3,5,6,7,8,9,9,5,3,3,6]))
[4, 6, 8, 6]
>>> filter(lambda x : x % 2 == 0, [4,3,5,6,7,8,9,9,5,3,3,6])
<filter object at 0x000001A9FE563970>
>>> tuple(filter(lambda x : x % 2 == 0, [4,3,5,6,7,8,9,9,5,3,3,6]))
(4, 6, 8, 6)
>>> 