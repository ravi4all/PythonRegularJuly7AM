a = 7
b = 8
c = a + b
print(c)
print('Sum is',c)
print("Sum of",a,"and",b,"is",c)

print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {0} is {2}".format(b,a,c))

#f-strings (fast strings)
print(f"Sum of {a} and {b} is {c}")

print(f"Sum of {a=} and {b=} is {c=}")
