import random

comp_choice = ["rock", "paper", "scissor"]
#while True:
print("------------ ROCK-PAPER-SCISSOR-GAME -------------")
youwin = 0
computerwin = 0
for i in range(1, 6):
        print("----round ", i, " start -----")
        print("select any of the following option")
        print("1. rock")
        print("2. paper") 
        print("3. scissor")
        user = int(input())
        if user == 1:
            print("You select : rock")
            user = "rock"
        elif user == 2:
            print("You select : paper")
            user = "paper"
        elif user == 3:
            print("You select : scisssor")
            user = "scissor"
        else:
            print("INVALID ENTRY")
            break
        computer_choice = random.choice(comp_choice)
        print("Computer selects :", computer_choice)

        if user == computer_choice:
            print("this is drawn")
        elif (user == "rock" and computer_choice == "scissor") or (
                user == "scissor" and computer_choice == "paper") or (user == "paper" and computer_choice == "rock"):
            print("*********** YOU WIN !!!!***********")
            youwin = youwin + 1
        else:
            print("********* COMPUTER WIN !!!**********")
            computerwin = computerwin + 1

        if youwin > computerwin:
            print(" YOU WIN THE GAME !!!!")
            print("Your score :", youwin)
            print("Computer score :", computerwin)

        elif computerwin > youwin:
            print(" YOU LOST THE GAME !!!!")
            print("Your score :", youwin)
            print("Computer score :", computerwin)

        else:
            print("MATCH DRAWN")

        option = input("Want to play again ? (yes or no)")

        if option == "yes":
            continue
        else:
            break