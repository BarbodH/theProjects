import random

answer = random.randint(1 , 100)
while True:
    try: 
        guess_count = int(input("How many times do you wanna play? "))
        print("Enter a number between 1 and 100: ")
        for _ in range(guess_count):
            choice = int(input())
            if answer > choice:
                print("Enter a larger number: ")
            elif answer < choice:
                print("Enter a smaller number: ")
            else:
                print("")
                print("YOU WON!!!")
        if answer != choice:
            print("")
            print(f"Game Over! The correct answer is: {answer}")
            break

    except ValueError:
        print("Enter an integer!")