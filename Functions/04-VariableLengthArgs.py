# Variable Length Arguments
# def add(*x):
#     # print(x)
#     sum = 0
#     for i in x:
#         sum += i
#     print(sum)
#
# add(5,6)
# add(4,5,7,8)
# add(3,4,6,8,9,4,5,7)

# Keyword variable length
def person(**details):
    print(details)

person(name = 'Ram', age = 45)
person(name = 'Shyam', age = 47, sal = 56000, dept = 'IT')








