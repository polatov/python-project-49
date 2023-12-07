import random


GAME_DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    correct_answer = gcd(number1, number2)
    question = f'Question: {number1} {number2}'
    return question, correct_answer
