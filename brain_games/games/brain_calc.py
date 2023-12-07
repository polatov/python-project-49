import random


GAME_DESCRIPTION = "What is the result of the expression?"


def generate_round():
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
    question = f'Question: {number_1} {op} {number_2}'
    return question, correct_answer
