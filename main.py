import random
import sys
from colorama import Back, Fore, init


def is_draw(board: list[list[str]]) -> bool:
    # TODO: try to implement
    #  порахувати скільки пробілів у board
    #  якщо пробілів 0, то це нічия
    pass


def print_board(board: list[list[str]]):
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |", end="\n")


def put_mark_on_board(board: list[list[str]], player: str):
    # try to implement
    row = int(input("рядок: "))
    column = int(input("стовпчик: "))
    if board[row-1][column-1] == " ":
        board[row-1][column-1] = player
    else:
        print("Це місце зайняте. Спробуйте інше")
        put_mark_on_board(board, player)


def is_win(board: list[list[str]], player: str) -> bool:
    """
    | X | X | X |
    |   |   |   |
    |   |   |   |
    —————————————
    """
    # перший рядок
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    # другий рядок
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    # третій рядок
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    # перший стовпчик
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    # другий стовпчик
    elif board[0][1] == player and board[1][1] == player and board[2][2] == player:
        return True
    # третій стовпчик
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    # головна діагональ
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    else:
        return False


if __name__ == '__main__':
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    player = 'O'                # get a random player

    # game loop
    while not is_draw(board):
        if player == "X":
            player = "O"
        else:
            player = "X"
        put_mark_on_board(board, player)
        print_board(board)
        if is_win(board, player):
            # greet a player with a win
            print(f"Player: {player} win!")
            break
    else:
        # tell that it is a draw
        print("Draw :[")

    print("Thank you for playing")


