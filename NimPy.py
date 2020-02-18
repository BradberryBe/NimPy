from random import random
# Implementation of the game of nim in python
# This implementation has the computer player win every time.
# In this implementation, taking the last token causes the player to lose
# Ben Bradberry
# 2/18/20

tokens = 21

def getPlayerMove(name):
    invalid = True
    global tokens
    while(invalid):
        taken = input("How many tokens do you take?: ")
        taken = int(taken)
        if (taken > 3 or taken < 1):
            print("Invalid number of tokens: ", taken)
        elif (tokens - taken < 0):
            print("Not enough remaining tokens, can only take max ", tokens)
        else:
            invalid = False
    tokens = tokens - taken
    

def getOpponentMove(name):
    global tokens
    best = (tokens % 4) - 1
    if (best < 0):                              # subtracts max number of tokens possible            
        best = 3
    if (best == 0):                             # subtracts random number of tokens
        best = random.randint(1, 3)
    if (tokens <= 4 and tokens < 1):            # leaves only one token left            
        best = tokens - 1
    if (tokens == 1):                           # only one token left, so bot has to take 1
        best = 1

    tokens = tokens - best
    print(name, " picks ", best, " token(s).")



def main():

    global tokens
    cpuName = "NIM bot 3000"
    play = True

    print("The game of Nim\n")
    playerName = input ("What is your name?: ")
    turnChoice = input("Will you go first? (Y/N): ")

    #Normalize the input
    turnChoice = turnChoice.lower().strip()

    if (turnChoice == "y" or turnChoice == "yes"):
        while (play):
            print("TOKENS LEFT ", tokens)
            getPlayerMove(playerName)
            if (tokens == 0):
                print(cpuName, " Wins!")
                play = False
                break
            print("TOKENS LEFT ", tokens)
            getOpponentMove(cpuName)
            if (tokens == 0):
                print(playerName, " Wins!")
                play = False
                break            
    else:
        while (play):
            print("TOKENS LEFT ", tokens)
            getOpponentMove(cpuName)
            if (tokens == 0):
                print(playerName, "Wins!")
                play = False
                break
            print("TOKENS LEFT ", tokens)
            getPlayerMove(playerName)
            if (tokens == 0):
                print(cpuName, "Wins!")
                play = False
                break


if __name__== '__main__':
    main()