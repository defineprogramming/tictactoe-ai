# Importing modules
import random
import numpy as np

# Defining constants
BOARD_SIZE = 3 # The size of the board (3x3)
EMPTY = 0 # The value for an empty cell
X = 1 # The value for X player
O = -1 # The value for O player
WIN_SCORE = 1 # The reward for winning a game
DRAW_SCORE = 0.5 # The reward for drawing a game
LOSE_SCORE = 0 # The reward for losing a game

# Defining helper functions

def print_board(board):
    """Prints the board in a human-readable format"""
    symbols = {EMPTY: " ", X: "X", O: "O"} # A dictionary to map values to symbols
    print("-" * (BOARD_SIZE * 2 + 1)) # Print a horizontal line
    for i in range(BOARD_SIZE): # For each row
        print("|", end="") # Print a vertical line
        for j in range(BOARD_SIZE): # For each column
            print(symbols[board[i][j]] + "|", end="") # Print the symbol and a vertical line
        print() # Print a newline
        print("-" * (BOARD_SIZE * 2 + 1)) # Print a horizontal line

def get_empty_cells(board):
    """Returns a list of tuples representing the coordinates of the empty cells on the board"""
    empty_cells = [] # Initialize an empty list
    for i in range(BOARD_SIZE): # For each row
        for j in range(BOARD_SIZE): # For each column
            if board[i][j] == EMPTY: # If the cell is empty
                empty_cells.append((i, j)) # Append its coordinates to the list
    return empty_cells

def check_winner(board):
    """Returns the winner of the board, or None if there is no winner yet"""
    sums = [] # Initialize an empty list to store the sums of each row, column and diagonal
    
    for i in range(BOARD_SIZE): 
        sums.append(sum(board[i])) # Add the sum of each row
    
    for j in range(BOARD_SIZE):
        sums.append(sum(board[:, j])) # Add the sum of each column
    
    sums.append(sum(board.diagonal())) # Add the sum of the main diagonal
    
    sums.append(sum(np.fliplr(board).diagonal())) 
    	# Add the sum of the anti-diagonal (flip left-right and then take diagonal)

    
    if X * BOARD_SIZE in sums: 
    	# If there is a sum equal to X times the board size, X has won
        
        return X 
    
    elif O * BOARD_SIZE in sums: 
    	# If there is a sum equal to O times the board size, O has won
        
        return O 
    
    else: 
    	# Otherwise, there is no winner yet
        
        return None


def check_game_over(board):
    
"""Returns True if the game is over (either someone has won or there are no more moves), False otherwise"""
    
winner = check_winner(board) 
    
	# Check if there is a winner
    
if winner is not None: 
        
	# If there is a winner, the game is over
        
	return True 
    
else: 
        
	empty_cells = get_empty_cells(board) 
        
		# Get the list of empty cells
        
	if len(empty_cells) == 0: 
            
			# If there are no more empty cells, the game is over
            
			return True 
        
	else: 
            
			# Otherwise, the game is not over
            
			return False


def get_score(winner):
    
"""Returns the score based on who won"""
    
if winner == X:
        
	return WIN_SCORE 
    
elif winner == O:
        
	return LOSE_SCORE 
    
else:
        
	return DRAW_SCORE


def human_move(board):
    
"""Asks the human player to enter their move and updates the board accordingly"""
    
valid_move = False 
    
while not valid_move:
        
	try:
            
			row = int(input("Enter row (1-3): ")) - 1 
            
				# Ask for row and subtract one to get zero-based index
            
			col = int(input("Enter column (1-3): ")) - 1 
            
				# Ask for column and subtract one to get zero-based index
            
			if (row, col) in get_empty_cells(board): 
                
# If the move is valid (the cell is empty)
                board[row][col] = X # Update the board with X
                valid_move = True # Set valid_move to True to exit the loop
            else:
                print("Invalid move. Try again.") # Otherwise, print an error message
        except ValueError:
            print("Invalid input. Try again.") # If the input is not an integer, print an error message

def ai_move(board):
    """Chooses a random move for the AI and updates the board accordingly"""
    empty_cells = get_empty_cells(board) # Get the list of empty cells
    random_cell = random.choice(empty_cells) # Choose a random cell from the list
    row, col = random_cell # Unpack the coordinates of the cell
    board[row][col] = O # Update the board with O

def update_q_table(q_table, state, action, reward, next_state):
    """Updates the Q-table using Q-learning algorithm"""
    alpha = 0.1 # The learning rate
    gamma = 0.9 # The discount factor
    
    max_next_q_value = max(q_table[next_state]) 
    	# Get the maximum Q-value for the next state
    
    current_q_value = q_table[state][action] 
    	# Get the current Q-value for the state-action pair
    
    new_q_value = current_q_value + alpha * (reward + gamma * max_next_q_value - current_q_value) 
    	# Calculate the new Q-value using Q-learning formula
    
    q_table[state][action] = new_q_value 
    	# Update the Q-table with the new Q-value

def ai_move_with_learning(board, q_table):
    
# Chooses a move for the AI using Q-learning and updates both the board and the Q-table accordingly
    epsilon = 0.1 # The exploration rate
    empty_cells = get_empty_cells(board) # Get the list of empty cells
    state = tuple(board.flatten()) # Convert the board to a tuple as the state
    
    if random.random() < epsilon: 
    	# With a probability of epsilon, choose a random move
        
        action = random.choice(empty_cells) # Choose a random cell from the list
        
    else: 
    	# Otherwise, choose the best move based on Q-values
        
        q_values = [q_table[state][cell] for cell in empty_cells] 
        	# Get the Q-values for each empty cell
        
        max_q_value = max(q_values) 
        	# Get the maximum Q-value
        
        best_actions = [cell for cell in empty_cells if q_table[state][cell] == max_q_value] 
        	# Get all the cells that have the maximum Q-value
        
        action = random.choice(best_actions) 
        	# Choose a random cell from the best actions
    
    row, col = action # Unpack the coordinates of the chosen cell
    board[row][col] = O # Update the board with O
    
    next_state = tuple(board.flatten()) # Convert the updated board to a tuple as the next state
    reward = get_score(check_winner(board)) # Get the reward based on who won (or None if not over yet)
    
    update_q_table(q_table, state, action, reward, next_state) 
# Update the Q-table using Q-learning algorithm

def play_game(q_table):
    """Plays a game of Tic Tac Toe between a human and an AI"""
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int) # Initialize an empty board
    print("Welcome to Tic Tac Toe!")
    print("You are X and the AI is O.")
    print_board(board) # Print the board
    
    game_over = False # Initialize a flag to indicate if the game is over
    
    while not game_over: # While the game is not over
        
        human_move(board) # Ask the human to make a move
        print_board(board) # Print the board
        
        game_over = check_game_over(board) # Check if the game is over
        
        if not game_over: # If the game is not over
            
            ai_move_with_learning(board, q_table) 
            	# Make a move for the AI using Q-learning
            
            print("AI moved:")
            print_board(board) # Print the board
            
            game_over = check_game_over(board) 
            	# Check if the game is over
    
    winner = check_winner(board) 
    	# Check who won
    
    if winner == X:
        
        print("You won!") 
    
    elif winner == O:
        
        print("You lost!") 
    
    else:
        
        print("It's a draw!")

def main():
    
"""The main function that runs multiple games and saves the Q-table"""
    
q_table = {} 
    	# Initialize an empty dictionary to store the Q-table
    
for i in range(1000): 
        
	# Play 1000 games
        
	play_game(q_table) 
        
		# Play one game and update the Q-table
        
	print(f"Game {i+1} finished.") 
        
		# Print a message after each game
        
np.save("q_table.npy", q_table) 
        
# Save the Q-table as a numpy file
    
print("All games finished. Q-table saved.") 
    	# Print a message after all games are finished

if __name__ == "__main__":
    
    main() # Call the main function
