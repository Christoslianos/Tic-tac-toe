import random

# A empty board
board = []


def create_board():
    for x in range(3):
        row = []
        for y in range(3):
            row.append('_')
        board.append(row)


def choose_player():
    return random.randint(0, 1)


# find the position on the board
def find_spot(row, col, player):
    board[row][col] = player


# check if the player is a winner
def is_player_winner(player):
    win = None
    n = len(board)

    # checking the rows
    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win
    # checking the columns
    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win
        # checking the diagonals
        win = True
        for i in range(n):
            if board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False


# check if the board is filled
def is_board_filled():
    for row in board:
        for item in row:
            if item == "_":
                return False
    return True


# swap players
def choose_players(player):
    return '0' if player == 'X' else 'X'


# show the board
def show_board():
    for row in board:
        for item in row:
            print(item, end="")
        print()


# start the game
def start():
    create_board()

    player = 'X' if choose_player() == 1 else '0'
    while True:
        print(f'It is your turn player {player}')

        show_board()
        # taking input from the players
        row, col = list(map(int, input("Enter row and column numbers to position: ").split()))
        print()

        # finding the spot
        find_spot(row - 1, col - 1, player)

        # check for a win
        if is_player_winner(player):
            print(f'Player {player} wins the round!')
            break
        if is_board_filled():
            print('Match is a draw')
            break

        player = choose_players(player)
    # show the score
    print()
    show_board()


start()
