# x = 10
# y = 20

def add(x,y):
    # x = 10
    # y = 20
    global z
    z = x + y
    print("Sum is",z)

def sub(x,y):
    # x = 10
    # y = 20
    z = x - y
    print("Sub is",z)

def mul(x,y):
    # x = 10
    # y = 20
    z = x * y
    print("Mul is",z)

add(10,20)
sub(11,22)
mul(5,7)

print(z)