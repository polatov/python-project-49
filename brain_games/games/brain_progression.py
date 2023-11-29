import random
import prompt


def play_brain_progression(name):
    correct_answers = 0
    print("What number is missing in the progression?")
    while correct_answers < 3:
        # Длина прогрессии
        length = random.randint(5, 10)

        # Шаг прогрессии
        step = random.randint(1, 10)

        # Первый элемент
        first_element = random.randint(1, 99)

        # Инициализация пустого списка для арифметической прогрессии
        number_line = []

        for i in range(length):
            next_element = first_element + i * step
            number_line.append(next_element)

        # Выбор случайного индекса для замены
        hidden_index = random.randint(0, length - 1)

        # Правильный ответ
        correct_answer = number_line[hidden_index]

        # Замена элемента на две точки
        number_line[hidden_index] = '..'

        # Вопрос
        print("Question: ", end='')
        for element in number_line:
            print(element, end=' ')
        print()

        # Ответ игрока
        user_answer = prompt.string("Your answer: ")

        if correct_answer == int(user_answer):
            print("Correct")
            correct_answers += 1

        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    return print(f"Congratulations, {name}!")
