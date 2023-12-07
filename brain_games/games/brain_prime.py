import random


GAME_DESCRIPTION = ("Answer \"yes\" if given number is prime. "
                    "Otherwise answer \"no\".")


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = random.randint(1, 99)
    question = f"Question: {number}"
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
