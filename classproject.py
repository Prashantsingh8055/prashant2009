import random

EMPTY = " "
HUMAN = "X"
AI = "O"  # used later if you enable basic AI

def make_board():
    # 3x3 2D list initialized to spaces
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    # Pretty CLI board printer
    for r in range(3):
        print(" | ".join(board[r]))
        if r < 2:
            print("-" * 9)

def is_move_valid(board, r, c):
    return 0 <= r < 3 and 0 <= c < 3 and board[r][c] == EMPTY

def place_move(board, r, c, mark):
    if is_move_valid(board, r, c):
        board[r][c] = mark
        return True
    return False

def check_winner(board):
    # Rows
    for r in range(3):
        row = board[r]
        if row[0] != EMPTY and row[0] == row[1] == row[2]:
            return row[0]
    # Cols
    for c in range(3):
        if board[0][c] != EMPTY and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # Diagonals
    if board[1][1] != EMPTY:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    return None

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def get_human_move():
    # Input as "row col" with 0-based indices (0..2)
    while True:
        raw = input("Enter your move as 'row col' (0-2 0-2): ").strip()
        parts = raw.split()
        if len(parts) != 2:
            print("Please enter two numbers like: 1 2")
            continue
        try:
            r, c = map(int, parts)
            return r, c
        except ValueError:
            print("Please enter integers between 0 and 2.")

def get_random_ai_move(board):
    # Basic AI placeholder: choose a random empty cell
    empties = [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]
    return random.choice(empties) if empties else None

def play_two_players():
    board = make_board()
    current = HUMAN  # X starts
    while True:
        print_board(board)
        print(f"{current}'s turn")
        r, c = get_human_move()
        if not place_move(board, r, c, current):
            print("Invalid move. Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current = AI if current == HUMAN else HUMAN

def play_vs_basic_ai():
    board = make_board()
    current = HUMAN  # human starts
    while True:
        print_board(board)
        if current == HUMAN:
            print("Your turn (X).")
            r, c = get_human_move()
            if not place_move(board, r, c, HUMAN):
                print("Invalid move. Try again.")
                continue
        else:
            print("AI's turn (O).")
            move = get_random_ai_move(board)
            if move is None:
                # Board full
                pass
            else:
                r, c = move
                place_move(board, r, c, AI)

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current = AI if current == HUMAN else HUMAN

if __name__ == "__main__":
    print("Tic-Tac-Toe (CLI)")
    mode = input("Choose mode: 1) Two Players  2) Vs Basic AI > ").strip()
    if mode == "2":
        play_vs_basic_ai()
    else:
        play_two_players()