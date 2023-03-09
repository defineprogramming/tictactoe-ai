import game
import ai

def main():
    # Initialize the board and the AI agent
    board = game.Board()
    agent = ai.Agent()

    # Choose who goes first: X or O
    turn = input("Do you want to play as X or O? ").upper()
    while turn not in ["X", "O"]:
        turn = input("Invalid choice. Please enter X or O: ").upper()

    # Play until the game is over
    while not board.is_over():
        # Print the board and the score
        print(board)
        print(f"Score: {board.score()}")

        # If it's the human's turn, get their move and update the board
        if turn == board.human:
            move = int(input("Enter your move (1-9): "))
            while not board.is_valid(move):
                move = int(input("Invalid move. Please enter a number between 1 and 9: "))
            board.update(move, turn)

        # If it's the AI's turn, get their move using reinforcement learning and update the board
        else:
            move = agent.get_move(board)
            board.update(move, turn)

        # Switch turns
        turn = "X" if turn == "O" else "O"

    # Print the final board and the score
    print(board)
    print(f"Score: {board.score()}")

    # Print the result of the game
    if board.winner() == board.human:
        print("You won!")
    elif board.winner() == board.ai:
        print("You lost!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
