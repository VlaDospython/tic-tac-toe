import random
import sys




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


