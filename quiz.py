quiz_data = {
    "questions": [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        {
            "question": "Which programming language is known as the language of the web?",
            "options": ["A) Python", "B) Java", "C) JavaScript", "D) C++"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Leo Tolstoy"],
            "answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "C"
        }
    ]
}

# Function to ask questions and check answers
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    
    if user_answer == question_data["answer"]:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer was {question_data['answer']}.\n")
        return 0

# Main function to run the quiz
def run_quiz():
    score = 0
    print("Welcome to the Quiz Application!\n")
    
    for question in quiz_data["questions"]:
        score += ask_question(question)
    
    print(f"Your final score is: {score}/{len(quiz_data['questions'])}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()