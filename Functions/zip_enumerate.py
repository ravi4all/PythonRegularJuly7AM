Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> emp_id = [101,102,103,104]
>>> emp_name = ["John","Mac","Sam","Max"]
>>> zip(emp_id, emp_name)
<zip object at 0x00000245CFE00FC0>
>>> list(zip(emp_id, emp_name))
[(101, 'John'), (102, 'Mac'), (103, 'Sam'), (104, 'Max')]
>>> emp_id = [101,102,103]
>>> list(zip(emp_id, emp_name))
[(101, 'John'), (102, 'Mac'), (103, 'Sam')]
>>> for i in range(len(names)):
	print(emp_name[i])

	
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    for i in range(len(names)):
NameError: name 'names' is not defined
>>> for i in range(len(emp_name)):
	print(emp_name[i])

	
John
Mac
Sam
Max
>>> for i in range(len(emp_name)):
	print(i, emp_name[i])

	
0 John
1 Mac
2 Sam
3 Max
>>> enumerate(emp_name)
<enumerate object at 0x00000245CFE4A380>
>>> list(enumerate(emp_name))
[(0, 'John'), (1, 'Mac'), (2, 'Sam'), (3, 'Max')]
>>> for i, name in enumerate(emp_name):
	print(i, name)

	
0 John
1 Mac
2 Sam
3 Max
>>> for id, name in zip(emp_id, emp_name)):
	
SyntaxError: unmatched ')'
>>> for id, name in zip(emp_id, emp_name)):
	
SyntaxError: unmatched ')'
>>> for id, name in zip(emp_id, emp_name):
	print(id, name)

	
101 John
102 Mac
103 Sam
>>> for i, id, name in enumerate(zip(emp_id, emp_name)):
	print(i, id, name)

	
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for i, id, name in enumerate(zip(emp_id, emp_name)):
ValueError: not enough values to unpack (expected 3, got 2)
>>> for i, data in enumerate(zip(emp_id, emp_name)):
	print(i, data)

	
0 (101, 'John')
1 (102, 'Mac')
2 (103, 'Sam')
>>> 