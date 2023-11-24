from random import randint
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import print_welcome_message


def brain_game(name):

    correct_answers = 0
    while correct_answers < 3:
        number = randint(1, 100)
        print("Question:", number)
        user_answer = prompt.string("Your answer: ")

        correct_answer = "no" if number % 2 else "yes"

        if user_answer == correct_answer:
            print("Correct")
            correct_answers += 1
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                  f"Let's try again, {name}!")
            return
    return print(f"Congratulations, {name}!")

def main():
    print_welcome_message()
    user_name = welcome_user()
    brain_game(user_name)

if __name__ == '__main__':
    main()
