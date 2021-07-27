num = int(input("Enter the number : "))

prime = True
for i in range(2, num//2):
    if num % i == 0:
        #print(num,"is not a prime number")
        prime = False
        break
    else:
        prime = True
        #print(num,"is a prime number")

if prime:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
