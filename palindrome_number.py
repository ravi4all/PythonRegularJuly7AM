num = int(input("Enter a number : "))
reverse = 0
temp = num

while(num > 0) {
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if(temp == reverse):
    print("Palindrome Number")
else:
    print("Not Palindrome")
