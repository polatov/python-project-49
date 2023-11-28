import random
import prompt


def play_brain_prime(name):
    correct_answers = 0
    print(f"Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    while correct_answers < 3:
        # Выбор числа
        number = random.randint(1, 99)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        if number % 2 != 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if user_answer == correct_answer:
            print("Correct")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    return print(f"Congratulations, {name}!")
