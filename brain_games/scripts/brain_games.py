#!/usr/bin/env python3

__package__ = 'brain_games'
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import brain_game


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    brain_game(user_name)


if __name__ == '__main__':
    main()
