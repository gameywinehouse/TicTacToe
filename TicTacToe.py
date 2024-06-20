import random

def display_board(board):
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

def check_for_winner(board, mark):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == mark:
            return True
    return False

def board_is_full(board):
    return all(spot in ['X', 'O'] for spot in board)

def computer_turn(board):
    available_spots = [index for index, spot in enumerate(board) if spot == ' ']
    return random.choice(available_spots)

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    player = 'X'
    
    while True:
        display_board(board)
        
        if player == 'X':
            move = int(input("Player X, choose your position (1-9): ")) - 1
        else:
            move = computer_turn(board)
            print(f"Computer (O) chooses position {move + 1}")
        
        if board[move] == ' ':
            board[move] = player
            if check_for_winner(board, player):
                display_board(board)
                print(f"Player {player} wins!")
                break
            elif board_is_full(board):
                display_board(board)
                print("It's a draw!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            if player == 'X':
                print("Invalid move, try again.")
    
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == 'yes':
        tic_tac_toe()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    tic_tac_toe()
