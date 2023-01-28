import random



class CPUPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        # This is a simple AI that just chooses a random empty space
        return random.choice([i for i in range(9) if board[i] == " "])

