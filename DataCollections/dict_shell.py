Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = [4,3,5,7,7,4,[4,3,6,78,2]]
>>> x = data.copy()
>>> x = data[:]
>>> data[0] = 100
>>> data
[100, 3, 5, 7, 7, 4, [4, 3, 6, 78, 2]]
>>> x
[4, 3, 5, 7, 7, 4, [4, 3, 6, 78, 2]]
>>> data[-1][0] = 40
>>> data
[100, 3, 5, 7, 7, 4, [40, 3, 6, 78, 2]]
>>> x
[4, 3, 5, 7, 7, 4, [40, 3, 6, 78, 2]]
>>> import copy
>>> y = copy.deepcopy(data)
>>> data[-1][0] = 400
>>> data
[100, 3, 5, 7, 7, 4, [400, 3, 6, 78, 2]]
>>> x
[4, 3, 5, 7, 7, 4, [400, 3, 6, 78, 2]]
>>> y
[100, 3, 5, 7, 7, 4, [40, 3, 6, 78, 2]]
>>> x = 5
>>> x = 5,
>>> type(x)
<class 'tuple'>
>>> x = 5,6,47,23,12,7
>>> x = (5,6,47,23,12,7)
>>> x
(5, 6, 47, 23, 12, 7)
>>> x[0]
5
>>> x[0] = 50
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x[0] = 50
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = name, age, salary = "John", 45, 67000
>>> data
('John', 45, 67000)
>>> name
'John'
>>> age
45
>>> salary
67000
>>> data
('John', 45, 67000)
>>> data = {"name" : "John", "age" : 67, "salary":67000}
>>> data
{'name': 'John', 'age': 67, 'salary': 67000}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    data[0]
KeyError: 0
>>> data["name"]
'John'
>>> data["age"]
67
>>> data["salary"]
67000
>>> data["address"] = "Delhi"
>>> data
{'name': 'John', 'age': 67, 'salary': 67000, 'address': 'Delhi'}
>>> data.keys()
dict_keys(['name', 'age', 'salary', 'address'])
>>> data.values()
dict_values(['John', 67, 67000, 'Delhi'])
>>> data.items()
dict_items([('name', 'John'), ('age', 67), ('salary', 67000), ('address', 'Delhi')])
>>> data.get("name")
'John'
>>> data.get("age")
67
>>> data["name"]
'John'
>>> data["age"]
67
>>> data["dept"]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    data["dept"]
KeyError: 'dept'
>>> data.get("dept")
>>> data.get("dept", "Not Available")
'Not Available'
>>> data.get("name", "Not Available")
'John'
>>> data.fromkeys(["name","age"])
{'name': None, 'age': None}
>>> data
{'name': 'John', 'age': 67, 'salary': 67000, 'address': 'Delhi'}
>>> data.fromkeys(["name","age","dept"])
{'name': None, 'age': None, 'dept': None}
>>> data.popitem()
('address', 'Delhi')
>>> data
{'name': 'John', 'age': 67, 'salary': 67000}
>>> data.pop("age")
67
>>> data
{'name': 'John', 'salary': 67000}
>>> data.setdefault("age")
>>> data
{'name': 'John', 'salary': 67000, 'age': None}
>>> data["age"] = 40
>>> data.setdefault("dept","IT")
'IT'
>>> data
{'name': 'John', 'salary': 67000, 'age': 40, 'dept': 'IT'}
>>> data.update({"address":"Delhi","Company":"TCS"})
>>> data
{'name': 'John', 'salary': 67000, 'age': 40, 'dept': 'IT', 'address': 'Delhi', 'Company': 'TCS'}
>>> data.fromkeys(["name","age"],value="X")
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    data.fromkeys(["name","age"],value="X")
TypeError: fromkeys() takes no keyword arguments
>>> data.fromkeys(["name","age"],"X")
{'name': 'X', 'age': 'X'}
>>> data.fromkeys(["name","age"],["X","Y"])
{'name': ['X', 'Y'], 'age': ['X', 'Y']}
>>> for item in data:
	print(item)

	
name
salary
age
dept
address
Company
>>> for item in data:
	print(item, data[item])

	
name John
salary 67000
age 40
dept IT
address Delhi
Company TCS
>>> for item in data:
	print(item, " : ", data[item])

	
name  :  John
salary  :  67000
age  :  40
dept  :  IT
address  :  Delhi
Company  :  TCS
>>> for item in data.values():
	print(item)

	
John
67000
40
IT
Delhi
TCS
>>> names = ["Ram","Shyam","Manoj","Mohit","Gopal"]
>>> dept = ["IT","HR","IT","HR","SALES"]
>>> address = ["delhi","pune","delhi","delhi","chennai"]
>>> data = {"names" : names, "dept" : dept, "address" :  address}
>>> data
{'names': ['Ram', 'Shyam', 'Manoj', 'Mohit', 'Gopal'], 'dept': ['IT', 'HR', 'IT', 'HR', 'SALES'], 'address': ['delhi', 'pune', 'delhi', 'delhi', 'chennai']}
>>> data["names"]
['Ram', 'Shyam', 'Manoj', 'Mohit', 'Gopal']
>>> data["names"][0]
'Ram'
>>> data = [{"name":"Ram","dept":"IT","address":"chennai"},{"name":"Gopal","dept":"HR","address":"delhi"},{"name":"Shyam","dept":"IT","address":"chennai"},{"name":"Raman","dept":"IT","address":"pune"}]
>>> data
[{'name': 'Ram', 'dept': 'IT', 'address': 'chennai'}, {'name': 'Gopal', 'dept': 'HR', 'address': 'delhi'}, {'name': 'Shyam', 'dept': 'IT', 'address': 'chennai'}, {'name': 'Raman', 'dept': 'IT', 'address': 'pune'}]
>>> data[0]
{'name': 'Ram', 'dept': 'IT', 'address': 'chennai'}
>>> data[0]["name"]
'Ram'
>>> type(data)
<class 'list'>
>>> 