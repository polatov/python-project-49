from brain_games.engine import run_game
import brain_games.games.brain_gcd as brain_gcd


def main():
    run_game(brain_gcd.play_brain_gcd)


if __name__ == '__main__':
    main()
