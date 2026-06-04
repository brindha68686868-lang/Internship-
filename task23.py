# Quiz Application

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Processing Unit",
            "C. Central Program Utility",
            "D. Control Processing Unit"
        ],
        "answer": "A"
    }
]

score = 0

print("=== Welcome to the Quiz Application ===\n")

for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}\n")

print("=== Quiz Completed ===")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Grade: Excellent")
elif percentage >= 50:
    print("Grade: Good")
else:
    print("Grade: Needs Improvement")