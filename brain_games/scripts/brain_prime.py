from brain_games.scripts.brain_games import print_welcome_message
from brain_games.cli import welcome_user
from brain_games.games.brain_prime import play_brain_prime


def main():
    print_welcome_message()
    user_name = welcome_user()
    play_brain_prime(user_name)


if __name__ == '__main__':
    main()
