import random
import math


def play_brain_gcd():
    first_question = "Find the greatest common divisor of given numbers."
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    correct_answer = math.gcd(number1, number2)
    internal_question = f'Question: {number1} {number2}'
    return first_question, internal_question, correct_answer
