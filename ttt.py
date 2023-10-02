board = [" " for _ in range(9)]
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")
def is_game_over(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    if " " not in board:
        return True
    return False

current_player = "X"
while True:
    print_board(board)
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    if board[move] == " ":
        board[move] = current_player
        if is_game_over(board):
            print_board(board)
            if " " not in board:
                print("It's a tie!")
            else:
                print(f"Player {current_player} wins!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Invalid move. Try again.")
