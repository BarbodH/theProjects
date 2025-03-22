import random

def main():
    level = get_level()  # Get the level from the user
    score = 0  # Initialize score

    # Generate and ask 10 questions
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        
        # Ask the question and give the user up to 3 tries
        for attempt in range(3):
            try:
                user_answer = int(input(f"What is {x} + {y} = ? "))
                if user_answer == correct_answer:
                    score += 1  # Correct answer, increase score
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")  # Handle if input is not an integer

            if attempt == 2:  # After 3 wrong attempts, show the correct answer
                print(f"The correct answer is {correct_answer}")

    print(f"Your score: {score}/10")  # Output the score


def get_level():
    # Keep asking for a valid level
    while True:
        try:
            level = int(input("Enter level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_integer(level):
    # Generate a random integer based on the level
    if level == 1:
        return random.randint(0, 9)  # 1-digit number
    elif level == 2:
        return random.randint(0, 99)  # 2-digit number
    elif level == 3:
        return random.randint(0, 999)  # 3-digit number
    else:
        raise ValueError("Invalid level")  # Raise error if level is invalid


if __name__ == "__main__":
    main()