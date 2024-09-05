import csv
import random

def main():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        # skip the header
        next(reader)
        capitals = {row[0].rstrip(): row[1].rstrip() for row in reader}
    score = 0
    questions_answered = 0
    correct_answers = 0
    while True:
        state = random.choice(list(capitals.keys()))
        answer = input(f"What is the capital of {state}?\n")
        if answer.lower() == capitals[state].lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {capitals[state]}")
        questions_answered += 1
        score = correct_answers / questions_answered
        print(f"Your score is now {score:.2%}")


if __name__ == '__main__':
    main()
