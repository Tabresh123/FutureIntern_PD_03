import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Initialize the game state
        self.board = [' '] * 9  # 3x3 board
        self.current_player = 'X'
        
        # Create a 3x3 grid of buttons
        self.buttons = [tk.Button(root, text=' ', font=('normal', 40), width=5, height=2, command=lambda i=i: self.make_move(i)) for i in range(9)]

        # Layout buttons in a 3x3 grid
        for i, button in enumerate(self.buttons):
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col)

    def make_move(self, index):
        """Handle a move made by the current player."""
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.display_winner(self.current_player)
            elif self.check_draw():
                self.display_draw()
            else:
                self.switch_player()

    def switch_player(self):
        """Switch the turn to the next player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        """Check if the current player has won."""
        win_conditions = [
            [0, 1, 2],  # Row 1
            [3, 4, 5],  # Row 2
            [6, 7, 8],  # Row 3
            [0, 3, 6],  # Column 1
            [1, 4, 7],  # Column 2
            [2, 5, 8],  # Column 3
            [0, 4, 8],  # Diagonal 1
            [2, 4, 6],  # Diagonal 2
        ]
        
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def check_draw(self):
        """Check if the game is a draw."""
        return ' ' not in self.board

    def display_winner(self, winner):
        """Display a message when a player wins."""
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()

    def display_draw(self):
        """Display a message when the game is a draw."""
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        """Reset the game state for a new game."""
        self.board = [' '] * 9
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ')

    def restart_game(self):
        """Allow the player to restart the game."""
        self.reset_game()

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
