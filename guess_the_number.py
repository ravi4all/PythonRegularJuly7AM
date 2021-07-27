import random

cpu = random.randint(1,100)

# guess the number in 5 chances
count = 0
game = True
while game:
    guess = int(input("Enter your guess : "))
    if cpu == guess:
        print("You have guessed it right...")
        game = False
    elif cpu > guess:
        print("You have guessed smaller number...")
    elif cpu < guess:
        print("You have guessed larger number...")
    else:
        print("Invalid Input...")
    count += 1
    print("Chances Left :",5-count)
    if count == 5:
        print("Game Over, You Lose, Number was",cpu)
        game = False
