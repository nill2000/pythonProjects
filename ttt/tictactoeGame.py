import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self):
        self.current_player = 'X'
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.check_winner()
            self.switch_player()

    def check_winner(self):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
                self.display_winner(self.board[row][0])

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                self.display_winner(self.board[0][col])

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.display_winner(self.board[0][0])

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.display_winner(self.board[0][2])

        # Check for a draw
        if all(self.board[row][col] != '' for row in range(3) for col in range(3)):
            self.display_draw()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def display_winner(self, player):
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        self.reset_game()

    def display_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.current_player = 'X'
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        for button in buttons:
            button.config(text='')

def on_button_click(row, col):
    game.make_move(row, col)
    buttons[row * 3 + col].config(text=game.current_player)

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the game instance
game = TicTacToeGame()

# Create buttons for the game board
buttons = []
for row in range(3):
    for col in range(3):
        button = tk.Button(window, width=10, height=5, font=("Helvetica", 20),
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        buttons.append(button)

# Start the main loop
window.mainloop()
