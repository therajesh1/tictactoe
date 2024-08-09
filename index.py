# Create a 3x3 board with empty spaces
# board = [" " for _ in range(9)]
board=[" "]*9
# Function to display the board
def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Function to check for a win
def check_win(player):
    # These are the winning positions
    if (board[0] == board[1] == board[2] == player) or (board[3] == board[4] == board[5] == player) or (board[6] == board[7] == board[8] == player) or (board[0] == board[3] == board[6] == player) or (board[1] == board[4] == board[7] == player) or (board[2] == board[5] == board[8] == player) or (board[0] == board[4] == board[8] == player) or (board[2] == board[4] == board[6] == player):
        return True
    return False

# Function to check for a tie (no empty spaces)
def check_tie():
    return " " not in board

# Main game function
def play_game():
    current_player = "X"
    
    # Keep playing until there's a win or a tie
    while True:
        print_board()
        move = int(input(" enter your move (0-8): "))
        
        if board[move] == " ":
            board[move] = current_player
        else:
            print("Spot already taken. Try again.")
            continue
        
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        
        if check_tie():
            print_board()
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

play_game()
