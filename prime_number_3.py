min_range = int(input("Enter the min range : "))
max_range = int(input("Enter the max range : "))

for num in range(min_range, max_range):
    for i in range(2, num//2):
        if num % i == 0:
            #print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
