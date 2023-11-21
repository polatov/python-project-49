from random import randint
import prompt


def brain_game(name):

    correct_answers = 0
    while correct_answers < 3:
        number = randint(1, 100)
        print("Question:", number)
        user_answer = prompt.string("Your answer: ")

        correct_answer = "no" if number % 2 else "yes"

        if user_answer == correct_answer:
            print("Correct")
            correct_answers += 1
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                  f"Let's try again, {name}!")
            return
    return print(f"Congratulations, {name}!")
