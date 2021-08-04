Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Hello World, This is Python Programming"
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello world, this is python programming'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.swapcase()
'hELLO wORLD, tHIS IS pYTHON pROGRAMMING'
>>> text.casefold()
'hello world, this is python programming'
>>> t1 = "Hello"
>>> t2 = "heLLO"
>>> t1 == t2
False
>>> t1.casefold()
'hello'
>>> t2.casefold()
'hello'
>>> t1.casefold() == t2.casefold()
True
>>> t1 = "hellβ"
>>> t1
'hellβ'
>>> t1.casefold()
'hellβ'
>>> t2 = "hellss"
>>> t1.casefold() == t2.casefold()
False
>>> text.index('i')
15
>>> text.count('i')
3
>>> text
'Hello World, This is Python Programming'
>>> text.index('i')
15
>>> text.index('i',16)
18
>>> text.index('i',19)
36
>>> text.find('i')
15
>>> text.find('i',16)
18
>>> text.find('i',19)
36
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.rindex('i')
36
>>> text.rfind('i')
36
>>> text.islower()
False
>>> text.isupper()
False
>>> text.isalpha()
False
>>> text.isalnum()
False
>>> text.isprintable()
True
>>> text
'Hello World, This is Python Programming'
>>> text.replace('Hello', 'Bye')
'Bye World, This is Python Programming'
>>> text
'Hello World, This is Python Programming'
>>> text.split() # tokenize
['Hello', 'World,', 'This', 'is', 'Python', 'Programming']
>>> text.split(',')
['Hello World', ' This is Python Programming']
>>> text.center(10)
'Hello World, This is Python Programming'
>>> text.center(20)
'Hello World, This is Python Programming'
>>> text.center(30)
'Hello World, This is Python Programming'
>>> len(text)
39
>>> text.center(40)
'Hello World, This is Python Programming '
>>> text.center(41)
' Hello World, This is Python Programming '
>>> text.center(51)
'      Hello World, This is Python Programming      '
>>> text = text.center(51)
>>> text
'      Hello World, This is Python Programming      '
>>> text = 'Hello World, This is Python Programming '
>>> text.center(51, '*')
'******Hello World, This is Python Programming *****'
>>> text = 'Hello World, This is Python Programming'
>>> text.center(51, '*')
'******Hello World, This is Python Programming******'
>>> text = text.center(51)
>>> text
'      Hello World, This is Python Programming      '
>>> #trim/strip
>>> text.strip()
'Hello World, This is Python Programming'
>>> text.lstrip()
'Hello World, This is Python Programming      '
>>> text.rstrip()
'      Hello World, This is Python Programming'
>>> text = '******Hello World, This is Python Programming******'
>>> text.strip('*')
'Hello World, This is Python Programming'
>>> text.startswith('T')
False
>>> text.startswith('H')
False
>>> text.startswith('*')
True
>>> text.endswith('*')
True
>>> text.endswith('?')
False
>>> 