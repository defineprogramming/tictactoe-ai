class Board:
    def __init__(self):
        # Initialize an empty board as a list of 9 strings
        self.board = [" "] * 9

        # Assign symbols for human and AI players
        self.human = "X"
        self.ai = "O"

    def __str__(self):
        # Return a string representation of the board
        return f"""
         {self.board[0]} | {self.board[1]} | {self.board[2]}
        ---+---+---
         {self.board[3]} | {self.board[4]} | {self.board[5]}
        ---+---+---
         {self.board[6]} | {self.board[7]} | {self.board[8]}
        """

    def is_valid(self, move):
        # Check if a move is valid (between 1 and 9) and available (not occupied by a symbol)
        return 1 <= move <= 9 and self.board[move - 1] == " "

    def update(self, move, symbol):
        # Update the board with a given move and symbol
        self.board[move - 1] = symbol

    def is_over(self):
        # Check if the game is over (either someone has won or there are no more moves left)
        return self.winner() != None or self.is_full()

    def is_full(self):
        # Check if the board is full (no more empty spaces)
        return " " not in self.board

    def winner(self):
        # Check if there is a winner and return their symbol (X or O) or None if there is no winner
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                return self.board[i]

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return self.board[i]
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]

        # No winner
        return None

    def score(self):
        # Return a score for the board based on who is winning
        # +1 for human win, -1 for AI win, 0 for tie or ongoing game
        if self.winner() == self.human:
            return 1
        elif self.winner() == self.ai:
            return -1
        else:
            return 0
