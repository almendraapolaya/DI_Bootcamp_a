#===========================
#Mini-Project - Tic tae Toe
#===========================

# Instructions:
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.

# Step 1: Representing the Game Board

# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).


# Step 2: Displaying the Game Board

# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.


# Step 3: Getting Player Input

# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.


# Step 4: Checking for a Winner

# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.


# Step 5: Checking for a Tie

# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.


# Step 6: The Main Game Loop

# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).


# Tips:

# Consider creating helper functions to break down the logic into smaller, manageable parts.
# Follow the single responsibility principle: each function should do one thing and do it well.
# Think about how to switch between players.
# Think about how you will store the player’s symbol.
    
def display_board(board):
    if not board or len(board) != 3:
        print("Invalid TIC TAC TOE board")
    print("TIC TAC TOE")
    print("*" * 15)
    for row in range(3):
        row_to_print = "*  "
        for col in range(len(board[0])):
            vertical = "|" if col != 2 else ""
            row_to_print += f" {board[row][col] }{vertical}"
        row_to_print += "  *"
        print(row_to_print)
    print("*" * 15)

def validate_choice(choice_str):
    # Assuming players are not familiar with code so will have 'normal' row/column numbers
    if not choice_str.isdigit():
        print("Please choose a digit between 1-3")
        return False
    choice = int(choice_str)
    if (choice < 1 or choice > 3):
        print("Choose a value between [1-3]")
        return False
    return True

def player_input(player, board):
    is_valid = False
    chosen_row = ""
    chosen_col = ""
    while not is_valid:
        chosen_row = input("Enter Row: ")
        is_valid = validate_choice(chosen_row)
    is_valid = False
    while not is_valid:
        chosen_col = input("Enter Column: ")
        is_valid = validate_choice(chosen_col)
    # Convert choice from 1-3 into 0-2
    chosen_row = int(chosen_row) - 1
    chosen_col = int(chosen_col) - 1
    if board[chosen_row][chosen_col] != " ":
        print("This position is already taken! Please choose again")
        chosen_row, chosen_col = player_input(player, board)
    return chosen_row, chosen_col

def is_same_symbols(symbol_list, player):
    for val in symbol_list:
        if val != player:
            return False
    return True

def check_win(board, player):
    # For 3x3 Tictactoe, there are 5 cells to check and it's enough
    # [0,0], [0,1], [0,2], [1,0], [2,0]
    # However it's kind of ugly code, so I preffered to make a more readable but wasteful code
    # We check every horizontal, then every vertical, then diagonals

    for row in range(len(board)):
        if is_same_symbols(board[row], player):
            return True
    
    for col in range(len(board[0])):
        vertical_list = [board[row][col] for row in range(3)]
        if is_same_symbols(vertical_list, player):
            return True
    # Check diagonals
    diagonal_1 = [board[i][i] for i in range(3)]
    if is_same_symbols(diagonal_1, player):
        return True
    diagonal_2 = [board[0][2], board[1][1], board[2][0]]
    if is_same_symbols(diagonal_2, player):
        return True
    
    return False

def check_tie(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == " ":
                return False
    return not (check_win(board, 'X') or check_win(board, 'O'))

def play():
    board = []
    for row in range(3):
        board.append([])
        for col in range(3):
            board[row].append(" ")
    # board_example = [["X", "X", "O"], ["O", "O", "X"], ["X", "O", "X"]]
    players = ['X', 'O']
    is_win = False
    is_tie = False
    game_end = False
    while not game_end:
        for player_symbol in players:
            display_board(board)
            print(f"It's players {player_symbol}'s turn!")
            row, col = player_input(player_symbol, board)
            board[row][col] = player_symbol
            is_win = check_win(board, player_symbol)
            is_tie = check_tie(board)
            if is_win or is_tie:
                game_end = True
                break
    display_board(board)

    if is_win:
        print(f"Congraluations player {player_symbol}!!! you won! have a great day! :D ")
    if is_tie:
        print(f"You're blocked :( the game is tied..")

play()









