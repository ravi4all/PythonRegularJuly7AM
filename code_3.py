#Input from user
# whenever we take input, data type is always str
name = input("Enter your name : ")
print("Hello " + name)

# so we need to type cast/convert the input
fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))
sum = fnum + snum
#print("Sum is",sum)

sub = fnum - snum
div = round(fnum / snum, 2)
mul = fnum * snum

print(f"""
Sum is {sum}
Sub is {sub}
Div is {div}
Mul is {mul}
""")
