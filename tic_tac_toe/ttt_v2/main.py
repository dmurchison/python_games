import tkinter as tk
from cpu_player import CPUPlayer



class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("200x200")
        self.create_widgets()
        self.player = "X"
        self.computer = "O"
        self.cpu_player = CPUPlayer(self.computer)
        self.board = [" " for i in range(9)]
        self.root.mainloop()


    def create_widgets(self):
        self.buttons = [tk.Button(self.root, width=5, height=2, command=lambda x=i: self.play(x)) for i in range(9)]
        for i in range(9):
            self.buttons[i].grid(row=i//3, column=i%3)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=3)


    def play(self, pos):
        if self.board[pos] != " ":
            return
        self.board[pos] = self.player
        self.buttons[pos].config(text=self.player)
        if self.check_win(self.player):
            self.result_label.config(text=f"Player {self.player} wins!")
            self.reset()
        elif self.check_tie():
            self.result_label.config(text="Tie!")
            self.reset()
        else:
            self.player, self.computer = self.computer, self.player
            self.computer_play()


    def computer_play(self):
        pos = self.cpu_player.get_move(self.board)
        self.board[pos] = self.computer
        self.buttons[pos].config(text=self.computer)
        if self.check_win(self.computer):
            self.result_label.config(text=f"Player {self.computer} wins!")
            self.reset()
        elif self.check_tie():
            self.result_label.config(text="Tie!")
            self.reset()
        else:
            self.player, self.computer = self.computer, self.player


    def check_win(self, player):
        win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for pos in win_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] == player:
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
