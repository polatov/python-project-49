#!/usr/bin/env python3

from brain_games.cli import welcome_user


def print_welcome_message():
    print("Welcome to the Brain Games!")


def main():
    print_welcome_message()
    welcome_user()


if __name__ == '__main__':
    main()
