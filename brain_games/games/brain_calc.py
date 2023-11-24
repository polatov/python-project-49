import random
import prompt
from brain_games.cli import welcome_user


def brain_calc(name):
    correct_answers = 0
    while correct_answers < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        operator = ['+', '-', '*']
        op = random.choice(operator)
        if op == '+':
            correct_answer = number_1 + number_2
        elif op == '-':
            correct_answer = number_1 - number_2
        elif op == '*':
            correct_answer = number_1 * number_2

        print(f'Question: {number_1} {op} {number_2}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer == int(user_answer):
            print('Correct!')
            correct_answers += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  f"Let's try again, {name}!")
            return
    return print(f"Congratulations, {name}!")
def main():
    user_name = welcome_user()
    brain_calc(user_name)

if __name__ == '__main__':
    main()


