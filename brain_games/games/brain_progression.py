import random


def play_brain_progression():
    first_question = "What number is missing in the progression?"

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
    internal_question = "Question: " + " ".join(map(str, number_line))

    return (first_question,
            internal_question,
            correct_answer)
