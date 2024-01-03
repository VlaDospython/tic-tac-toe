import random
import sys


def is_draw(board: list[list[str]]) -> bool:
    pass


def print_board(board: list[list[str]]):
    pass


def put_mark_on_board(board: list[list[str]], player: str):
    pass


def is_win(board: list[list[str]], player: str) -> bool:
    pass


if __name__ == '__main__':
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    player = random.choice('XY')                # get a random player

    # game loop
    while not is_draw(board):
        # TODO: change player
        print_board(board)
        put_mark_on_board(board, player)
        if is_win(board, player):
            # TODO: greet a player with a win
            break
    else:
        # tell that it is a draw
        print("Draw :[")

    print("Thank you for playing")


