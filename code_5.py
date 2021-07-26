num = int(input("Enter a number : "))

for i in range(1,11):
    print("{} x {} = {}".format(num, i, num*i))

for i in range(1,6):
    print('*' * i)

for i in range(10):
    print(' ' * (10 - i) + '*' * (2*i + 1))
