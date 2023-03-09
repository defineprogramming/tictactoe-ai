# Tic Tac Toe with Reinforcement Learning

This is a python script that lets you play tic tac toe against an AI agent that learns from its own actions and the feedback from the board. The AI agent uses reinforcement learning to update its value function after each move. It also uses exploration and exploitation to balance between trying new moves and choosing the best ones.

## How to run

To run this script, you need python 3 installed on your system. You can download it from [here](https://www.python.org/downloads/).

To play the game, simply run the main.py file in your terminal:

`python main.py`

You will be asked to choose whether you want to play as X or O. Then, you will enter your move by typing a number between 1 and 9, corresponding to the position on the board:

`     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9     `

The game will end when either you or the AI agent wins, or when there are no more moves left. The final board and score will be displayed.

## How it works

This script consists of four modules: main.py, game.py, ai.py, and utils.py.

- main.py: This is the entry point of the program. It imports the other modules and runs the game loop.
- game.py: This contains the class definition for the Board object. It handles the logic of the tic tac toe game, such as checking for valid moves, updating the board state, scoring the board, and determining the winner.
- ai.py: This contains the class definition for the Agent object. It uses reinforcement learning to learn from its own actions and the feedback from the board. It stores a value function that maps each board state to a value, and updates it after each move. It also uses exploration and exploitation to balance between trying new moves and choosing the best ones.
- utils.py: This contains some utility functions that are used by the other modules.

## Future improvements

Some possible improvements for this project are:

- Adding a graphical user interface (GUI) for a better user experience
- Saving and loading the value function from a file
- Implementing different reinforcement learning algorithms or parameters
- Adding more features or variations to the game
