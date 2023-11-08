import prompt


def welcome_user() -> object:
    """

    :rtype: object
    """
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
