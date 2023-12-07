import random


GAME_DESCRIPTION = ("Answer \"yes\" if the number is even, "
                    "otherwise answer \"no\".")


def is_even(a):
    if a % 2 == 0:
        return "yes"
    else:
        return "no"


def generate_round():
    number = random.randint(1, 100)
    correct_answer = is_even(number)
    question = f"Question: {number}"
    return question, correct_answer
