import random


def play_brain_even():
    first_question = ("Answer \"yes\" if the number is even, "
                      "otherwise answer \"no\".")
    number = random.randint(1, 100)
    correct_answer = "no" if number % 2 else "yes"
    internal_question = f"Question: {number}"
    return first_question, internal_question, correct_answer
