def available_moves(board):
    # Return a list of available moves on the board (empty spaces)
    return [i + 1 for i in range(9) if board[i] == " "]

def get_state(board):
    # Return a string representation of the board state
    return "".join(board)

def print_value_function(value_function):
    # Print the value function in a human-readable format
    for state, value in value_function.items():
        print(f"{state}: {value:.2f}")
