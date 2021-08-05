Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = [4,3,5,6,8,9,4,3]
>>> type(data)
<class 'list'>
>>> data = list()
>>> data = [4,3,5,6,8,9,4,3]
>>> data[0]
4
>>> data[1]
3
>>> data[0:5]
[4, 3, 5, 6, 8]
>>> data[-1]
3
>>> data[::-1]
[3, 4, 9, 8, 6, 5, 3, 4]
>>> dir(data)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> data = []
>>> data.append(6)
>>> data
[6]
>>> data.append(8)
>>> data
[6, 8]
>>> data.append(81)
>>> data
[6, 8, 81]
>>> data.append(13)
>>> data
[6, 8, 81, 13]
>>> data.append(10)
>>> data
[6, 8, 81, 13, 10]
>>> data.append(12,14,15,67,42)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    data.append(12,14,15,67,42)
TypeError: append() takes exactly one argument (5 given)
>>> data.extend(12,14,15,67,42)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    data.extend(12,14,15,67,42)
TypeError: extend() takes exactly one argument (5 given)
>>> data.append([12,14,15,67,42])
>>> data
[6, 8, 81, 13, 10, [12, 14, 15, 67, 42]]
>>> del data[-1]
>>> data
[6, 8, 81, 13, 10]
>>> data.extend([12,14,15,67,42])
>>> data
[6, 8, 81, 13, 10, 12, 14, 15, 67, 42]
>>> data[3]
13
>>> data[3] = 30
>>> data
[6, 8, 81, 30, 10, 12, 14, 15, 67, 42]
>>> data.insert(3,100)
>>> data
[6, 8, 81, 100, 30, 10, 12, 14, 15, 67, 42]
>>> data.pop()
42
>>> data
[6, 8, 81, 100, 30, 10, 12, 14, 15, 67]
>>> data.pop(4)
30
>>> data
[6, 8, 81, 100, 10, 12, 14, 15, 67]
>>> data.remove(2)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    data.remove(2)
ValueError: list.remove(x): x not in list
>>> data.remove(10)
>>> data
[6, 8, 81, 100, 12, 14, 15, 67]
>>> data.count(1)
0
>>> data.count(81)
1
>>> data.index(12)
4
>>> sorted(data)
[6, 8, 12, 14, 15, 67, 81, 100]
>>> sorted(data, reverse=True)
[100, 81, 67, 15, 14, 12, 8, 6]
>>> data
[6, 8, 81, 100, 12, 14, 15, 67]
>>> data.sort()
>>> data
[6, 8, 12, 14, 15, 67, 81, 100]
>>> data.sort(reverse=True)
>>> data
[100, 81, 67, 15, 14, 12, 8, 6]
>>> for i in range(len(data)):
	print(data[i])

	
100
81
67
15
14
12
8
6
>>> for i in range(len(data)):
	if data[i] % 2 == 0:
		print("{} is even".format(data[i]))

		
100 is even
14 is even
12 is even
8 is even
6 is even
>>> for item in data:
	if item % 2 == 0:
		print(item)

		
100
14
12
8
6
>>> data = []
>>> for i in range(1,51):
	if i % 2 == 0:
		data.append(i)

		
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> data = [i for i in range(1,11)]
>>> data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> data = [i**2 for i in range(1,11)]
>>> data
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> data = [i for i in range(1,21) if i % 2 == 0]
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> data = [(i,j) for i in range(1,6) for j in range(1,6) if i == j]
>>> data
[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
>>> data = []
>>> for i in range(1,6):
	for j in range(1,6:)
	
SyntaxError: invalid syntax
>>> for i in range(1,6):
	for j in range(1,6):
		if i == j:
			data.append((i,j))

			
>>> data
[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
>>> data = [2,3,1,4,6,8,8,12,45]
>>> x = data
>>> x[0] = 100
>>> x
[100, 3, 1, 4, 6, 8, 8, 12, 45]
>>> id(x)
2640456059840
>>> id(data)
2640456059840
>>> data
[100, 3, 1, 4, 6, 8, 8, 12, 45]
>>> x = data[:]
>>> id(x)
2640456692544
>>> id(data)
2640456059840
>>> data[0] = 10
>>> data
[10, 3, 1, 4, 6, 8, 8, 12, 45]
>>> x
[100, 3, 1, 4, 6, 8, 8, 12, 45]
>>> data = [4,5,6,3,3,[8,7,8,9,1]]
>>> x = data[:]
>>> data[0] = 10
>>> data
[10, 5, 6, 3, 3, [8, 7, 8, 9, 1]]
>>> x
[4, 5, 6, 3, 3, [8, 7, 8, 9, 1]]
>>> data[-1][0]
8
>>> data[-1][0] = 80
>>> data
[10, 5, 6, 3, 3, [80, 7, 8, 9, 1]]
>>> data
[10, 5, 6, 3, 3, [80, 7, 8, 9, 1]]
>>> x
[4, 5, 6, 3, 3, [80, 7, 8, 9, 1]]
>>> 