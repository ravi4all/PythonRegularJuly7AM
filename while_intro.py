a = 10
while a > 0:
    print(a)
    a -= 1

a = 10
while True:
    print(a)
    a -= 1
    if a == 5:
        break

a = 10
flag = True
while flag:
    print(a)
    a -= 1
    if a == 5:
        flag = False
