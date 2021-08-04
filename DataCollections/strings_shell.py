Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Hello World, This is Python Programming"
>>> type(text)
<class 'str'>
>>> text[0]
'H'
>>> text[12]
' '
>>> text[13]
'T'
>>> len(text)
39
>>> text[39]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    text[39]
IndexError: string index out of range
>>> text[38]
'g'
>>> id(text)
1860994841840
>>> #slicing/substring
>>> text[0:10]
'Hello Worl'
>>> text[10]
'd'
>>> text[:]
'Hello World, This is Python Programming'
>>> text[10:]
'd, This is Python Programming'
>>> text[10:100]
'd, This is Python Programming'
>>> text[:10]
'Hello Worl'
>>> text[0:20:2]
'HloWrd hsi'
>>> text[0:20:1]
'Hello World, This is'
>>> text[0:20:2]
'HloWrd hsi'
>>> text[10:1]
''
>>> text[10:1:-1]
'dlroW oll'
>>> text[10:0:-1]
'dlroW olle'
>>> text[10::-1]
'dlroW olleH'
>>> text[-1]
'g'
>>> text[-2]
'n'
>>> text[-10:-1]
'rogrammin'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> #text[lowerbound, upperbound, step]
>>> #text[lowerbound, upperbound, step = + 1]
>>> #text[upperbound, lowerbound, step = - 1]
>>> text[::-1]
'gnimmargorP nohtyP si sihT ,dlroW olleH'
>>> 