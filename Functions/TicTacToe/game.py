import random

winning_combinations = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

positions = [1,2,3,4,5,6,7,8,9]
occupied = []
def gameBoard():
    print("""
        {} | {} | {}
        -----------
        {} | {} | {}
        -----------
        {} | {} | {}
    """.format(positions[0],positions[1],positions[2],
               positions[3],positions[4],positions[5],
               positions[6],positions[7],positions[8]))

def checkWinner(ch, pos):
    for i in range(len(winning_combinations)):
        if pos in winning_combinations[i]:
            index = winning_combinations[i].index(pos)
            winning_combinations[i][index] = ch

    print(winning_combinations)

def userChance(ch):
    pos = int(input("Enter your position : "))
    positions[pos - 1] = ch
    occupied.append(pos)
    checkWinner(ch, pos)

def cpuChance(ch):
    pos = random.randint(1,9)
    if pos in occupied:
        print("Position Already Occupied")
        cpuChance(ch)
    else:
        print("CPU Moved at",pos)
        positions[pos - 1] = ch
        occupied.append(pos)
        checkWinner(ch, pos)

def main():
    gameBoard()
    user_ch = input("Enter your choice : ")
    if user_ch == "X":
        cpu_ch = '0'
    else:
        cpu_ch = 'X'

    while True:
        userChance(user_ch)
        gameBoard()
        cpuChance(cpu_ch)
        gameBoard()

main()