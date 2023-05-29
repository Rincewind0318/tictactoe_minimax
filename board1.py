import random

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

user_input_letter = None
computer_letter = None

PLAYER_X = 'X'
PLAYER_O = 'O'

WINNING_COMBINATIONS = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
    (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
    (1, 5, 9), (3, 5, 7)  # Diagonals
]


def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('_+_+_')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('_+_+_')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print()


def space_is_free(position):
    return board[position] == ' '


def check_draw():
    return not any(value == ' ' for value in board.values())


def check_win(letter):
    for combo in WINNING_COMBINATIONS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == letter:
            return True
    return False


def insert_letter(letter, position):
    if space_is_free(position):
        board[position] = letter
        print_board(board)
    else:
        if letter == user_input_letter:
            print("Player try to choose a position again")
            player_move()
        else:
            print("Computer has to choose another position")
            computer_move()

    if check_win(letter):
        print(f"The winner is {letter}")
        exit()
    if check_draw():
        print("It's a draw!")
        exit()


def player_move():
    position = None
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        position = input("Enter your position: ")
    insert_letter(user_input_letter, int(position))


def player_moves_first():
    while not check_win(user_input_letter):
        player_move()
        computer_move()


def computer_move():
    best_score = -float('inf')
    best_move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer_letter
            score = minimax(board, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    insert_letter(computer_letter, best_move)


def minimax(board, is_maximizing):
    if check_win(computer_letter):
        return 1
    elif check_win(user_input_letter):
        return -1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer_letter
                score = minimax(board, False)
                board[key] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = user_input_letter
                score = minimax(board, True)
                board[key] = ' '
                best_score = min(score, best_score)
        return best_score


def start():
    global user_input_letter
    global computer_letter

    while user_input_letter != PLAYER_X and user_input_letter != PLAYER_O:
        user_input_letter = input("Choose 'X' or 'O'").upper()
    if user_input_letter == PLAYER_X:
        computer_letter = PLAYER_O
        player_moves_first()
    else:
        computer_letter = PLAYER_X
        computer_move_first()


def computer_move_first():
    while not check_win(computer_letter):
        computer_move()
        player_move()


start()
