import prompt


def run_game(game_module):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(game_module.GAME_DESCRIPTION)

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = game_module.generate_round()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == str(user_answer).strip():
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    return print(f"Congratulations, {user_name}!")
