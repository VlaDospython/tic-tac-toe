import random
import sys
# TODO: from colorama import init, Fore, Back


def is_draw(board: list[list[str]]) -> bool:
    pass


def print_board(board: list[list[str]]):
    pass


def put_mark_on_board(board: list[list[str]], player: str):
    pass


def is_win(board: list[list[str]], player: str) -> bool:
    pass


if __name__ == '__main__':
    congratulations = ["Nice!", "Amazing!", "Great!", "That`s wonderful!", "Excellent!", "Well done!", "Perfect!"]

    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    player = random.choice('XY')                # get a random player

    # game loop
    while not is_draw(board):
        # change player
        if player == "X":
            player = "Y"
        else:
            player = "X"

        print_board(board)
        put_mark_on_board(board, player)

        if is_win(board, player):
            # greet a player with a win
            print(f"{random.choice(congratulations)} You win!")
            break
    else:
        # tell that it is a draw
        print("Draw :[")

    print("Thank you for playing")


