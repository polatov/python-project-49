import random
import prompt


def play_brain_even(name):
    correct_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")

        correct_answer = "no" if number % 2 else "yes"

        if user_answer == correct_answer:
            print("Correct")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    return print(f"Congratulations, {name}!")
