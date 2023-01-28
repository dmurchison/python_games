import tkinter as tk
import random



# A simple 2 player Tic-Tac-Toe game, Don't look at the screen and cheat!

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("500x500")
        self.create_widgets()
        self.player_x = "X"
        self.player_o = "O"
        self.board = [" " for i in range(9)]
        self.root.mainloop()


    def create_widgets(self):
        self.buttons = [tk.Button(self.root, width=5, height=2, command=lambda x=i: self.play_x(x)) for i in range(9)]
        for i in range(9):
            self.buttons[i].grid(row=i//3, column=i%3)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=3)


    def play_x(self, pos):
        if self.board[pos] != " ":
            return
        self.board[pos] = self.player_x
        self.buttons[pos].config(text=self.player_x)
        if self.check_win(self.player_x):
            self.result_label.config(text=f"Player {self.player_x} wins!")
            self.reset()
        elif self.check_tie():
            self.result_label.config(text="Tie!")
            self.reset()
        else:
            self.player_x, self.player_o = self.player_o, self.player_x


    def play_o(self, pos):
        self.board[pos] = self.player_o
        self.buttons[pos].config(text=self.player_o)
        if self.check_win(self.player_o):
            self.result_label.config(text=f"Player {self.player_o} wins!")
            self.reset()
        elif self.check_tie():
            self.result_label.config(text="Tie!")
            self.reset()
        else:
            self.player_x, self.player_o = self.player_o, self.player_x


    def check_win(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for cond in win_conditions:
            if self.board[cond[0]] == player and self.board[cond[1]] == player and self.board[cond[2]] == player:
                return True
        return False


    def check_tie(self):
        return " " not in self.board


    def reset(self):
        self.board = [" " for i in range(9)]
        for button in self.buttons:
            button.config(text="")



if __name__ == "__main__":
    TicTacToe()

