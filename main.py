def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print("\n")

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6] 
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

board = [" "] * 9
player = "X"

while " " in board:
    print_board(board)
    move = int(input(f"Player {player}, choose your position (0-8): "))
    
    if board[move] == " ":
        board[move] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            break
        player = "O" if player == "X" else "X"
    else:
        print("Invalid move, try again.")

if " " not in board and not winner:
    print("It's a tie!")

