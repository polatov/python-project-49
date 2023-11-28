import random
import prompt
import math

def play_brain_gcd(name):
    correct_answers = 0
    print("Find the greatest common divisor of given numbers.")
    while correct_answers < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        correct_gcd = math.gcd(number1, number2)


        # Вопрос игроку
        print(f'Question: {number1} {number2}')

        # Ответ игрока
        user_answer = prompt.string('Your answer: ')
        if int(user_answer) == correct_gcd:
            correct_answers += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_gcd}.\n"
                  f"Let's try again, {name}!")
            return
    return print(f"Congratulations, {name}!")