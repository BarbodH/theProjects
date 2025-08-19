import random

answer = random.randint(1, 100)

guess_limit = int(input("How many times do you wanna play? "))

print("Guess a number between 1 and 100: ")

count = 0
while count <= guess_limit:
    choice = int(input())
    count += 1
    if choice == answer:
        print("You Won!")
        print(f"You guessed it in {count} {'try' if count == 1 else 'tries'}!")
        break
    elif answer > choice:
        print("Enter a larger number: ")
    else:
        print("Enter a smaller number: ")
else:
    print(f"Game Over! The correct answer is {answer}.")
