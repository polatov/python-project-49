import random


def play_brain_calc():
    first_question = "What is the result of the expression?"
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
    internal_question = f'Question: {number_1} {op} {number_2}'
    return first_question, internal_question, correct_answer
