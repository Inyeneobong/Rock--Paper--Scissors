import random

print("Welcome to Rock, Paper, Scissors by Sahib!")
print("------------------------------------------")

### Set up Variables
CPUscore = 0
Playerscore = 0
Tiescore = 0
PossibleHands = ["R", "P", "S"]

def CheckForWinner(Player,CPU):
    if(Player =="R" and CPU =="P"):
        print("Sorry you lost :(")
        return "CPU"
    elif(Player == "R" and CPU == "S"):
        print("Congrats! You have Won :)")
        return "Player"
    elif(Player == "P" and CPU == ""):
        print("Sorry, you lost")
        return "CPU"
    elif(Player == "P" and CPU == "R"):
        print("Congrats! You Won :)")
        return "Player"
    elif(Player == "S" and CPU == "R"):
        print("Sorry, you lost")
        return "CPU"
    elif(Player == "S" and CPU == "P"):
        print("Congrats! You Won :)")
        return "Player"
    else:
        print("It's a tie, Play again!")
        return "Tie"

### Start game loop
while(Playerscore !=3 and CPUscore !=3):
    ### Validate input
    while True:
        Player = input("\nPick a hand. R, P, or S: ")
        if(Player == "R" or Player == "P" or Player == "S"):
            break
        else:
            print("Invalid Input. Try again")

    ### Generate computer pick
    CPU = random.choice(PossibleHands)

    ### Print results
    print("Your hand: ", Player)
    print(" CPU hand: ", CPU)
    result = CheckForWinner(Player, CPU)
    if(result == "Player"):
        Playerscore += 1
    elif(result == "CPU"):
        CPUscore += 1
    else:
        Tiescore += 0
    print("Your score: ", Playerscore, "CPU: ", CPUscore)

print("Game Over! Thank you for playing :)")