a,b,c = 10,20,30

# Logical Operators - and (&), or (|), not (!)
if a > b and a > c:
    print("A is greatest")
elif b > a and b > c:
    print("B is greatest")
else:
    print("C is greatest")


print("Odd Even Program...............")
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

num = 10
if num % 2 == 0:print("Even")
else:print("Odd")

print("If Else Expression")
result = "Even" if num % 2 == 0 else "Odd"
print(result)

print("Greatest of 3 Using Expression")
result = "A" if a > b and a > c else "B" if b > a and b > c else "C"
print(result,"is greatest")




