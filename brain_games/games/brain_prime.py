import random


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def play_brain_prime():
    first_question = ("Answer \"yes\" if given number is prime. "
                      "Otherwise answer \"no\".")
    number = random.randint(1, 99)
    internal_question = f"Question: {number}"
    correct_answer = 'yes' if is_prime(number) else 'no'
    return first_question, internal_question, correct_answer
