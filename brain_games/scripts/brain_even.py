from brain_games.engine import run_game
import brain_games.games.brain_even as brain_even


def main():
    run_game(brain_even.play_brain_even)


if __name__ == '__main__':
    main()
