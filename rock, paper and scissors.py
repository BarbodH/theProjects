import random

computerChoice = random.choice(["rock" , "paper" , "scissors"])

choice_count = int(input("How many times do you wanna play? "))

for _ in range(1 , choice_count + 1):
    choice = input("Rock, paper or scissors? ").lower()
    if choice == "rock" or choice == "paper" or choice == "scissors":
        if computerChoice == "rock" and choice == "rock":
            print("Equal!")
            print("Computer's choice: " , computerChoice)
            print("Your choice: " , choice)
        elif computerChoice == "rock" and choice == "paper":
            print("You Won!")
            print("Computer's choice: " , computerChoice)
            print("Your choice: " , choice)
        elif computerChoice == "rock" and choice == "scissors":
            print("You Lost!")
            print("Computer's choice: " , computerChoice)
            print("Your choice: " , choice)
        elif computerChoice == "paper" and choice == "rock":
            print("You Lost!")
            print("Computer's choice: " , computerChoice)
            print("Your choice: " , choice)
        elif computerChoice == "paper" and choice == "paper":
            print("Equal!")
            print("Computer's choice: " , computerChoice)
            print("Your choice: " , choice)
        elif computerChoice == "paper" and choice == "scissors":
            print("You Won!")
            print("Computer's choice: " , computerChoice)
            print("Your choice: " , choice)
        elif computerChoice == "scissors" and choice == "rock":
            print("You Won!")
            print("Computer's choice: " , computerChoice)
            print("Your choice: " , choice)
        elif computerChoice == "scissors" and choice == "paper":
            print("You Lost!")
            print("Computer's choice: " , computerChoice)
            print("Your choice: " , choice)
        elif computerChoice == "scissors" and choice == "scissors":
            print("Equal!")
            print("Computer's choice: " , computerChoice)
            print("Your choice: " , choice)
    else:
        print("Entered a wrong input! enter rock, paper or scissors.")       

    

if choice_count == choice_count:
    print("")
    print("Done! See you next time 😊")

