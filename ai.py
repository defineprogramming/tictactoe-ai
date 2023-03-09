import random
import copy

class Agent:
    def __init__(self):
        # Initialize an empty value function as a dictionary
        self.value_function = {}

        # Initialize a learning rate (alpha) and a discount factor (gamma)
        self.alpha = 0.1
        self.gamma = 0.9

        # Initialize an exploration rate (epsilon) and a decay rate (lambda)
        self.epsilon = 0.5
        self.lambda_ = 0.99

    def get_move(self, board):
        # Get the best move for the current board state using epsilon-greedy strategy
        # With probability epsilon, choose a random move
        if random.random() < self.epsilon:
            move = random.choice(board.available_moves())
        
        # With probability 1 - epsilon, choose the move with the highest value
        else:
            move = self.max_value_move(board)

        # Decay the exploration rate over time
        self.epsilon *= self.lambda_

        # Return the chosen move
        return move

    def max_value_move(self, board):
        # Find the move that leads to the board state with the highest value
        # If there are multiple moves with the same value, choose one randomly
        max_value = -float("inf")
        max_moves = []
        for move in board.available_moves():
            # Make a copy of the board and update it with the move
            new_board = copy.deepcopy(board)
            new_board.update(move, board.ai)

            # Get the value of the new board state
            value = self.get_value(new_board)

            # Update the max value and max moves
            if value > max_value:
                max_value = value
                max_moves = [move]
            elif value == max_value:
                max_moves.append(move)

        # Return a random move from the max moves
        return random.choice(max_moves)

    def get_value(self, board):
        # Get the value of a board state from the value function
        # If the board state is not in the value function, initialize it with a small random number
        state = board.get_state()
        if state not in self.value_function:
            self.value_function[state] = random.uniform(-0.01, 0.01)
        return self.value_function[state]

    def update_value(self, old_board, new_board):
        # Update the value of the old board state based on the new board state and the reward
        # Use the temporal difference (TD) learning formula: V(s) <- V(s) + alpha * (reward + gamma * V(s') - V(s))
        old_state = old_board.get_state()
        new_state = new_board.get_state()
        reward = new_board.score()
        old_value = self.get_value(old_board)
        new_value = self.get_value(new_board)
        self.value_function[old_state] = old_value + self.alpha * (reward + self.gamma * new_value - old_value)
