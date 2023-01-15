from tkinter import *

App = Tk()
App.geometry('300x300')

title = Label(App, text='Tic Tac Toe')
title.grid(row=0, column=0, columnspan=3)

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

def button_click(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        button = Button(App, text='X', font=('Helvetica', 20), height=3, width=6)
        button.grid(row=row+1, column=col)
    else:
        print('Invalid move')



button_1 = Button(App, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(0, 0))
button_2 = Button(App, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(0, 1))
button_3 = Button(App, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(0, 2))
button_4 = Button(App, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(1, 0))
button_5 = Button(App, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(1, 1))
button_6 = Button(App, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(1, 2))
button_7 = Button(App, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(2, 0))
button_8 = Button(App, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(2, 1))
button_9 = Button(App, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(2, 2))

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)




def computer_move():
    # Find an empty cell
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                return


def button_click_x(row, col):
    # Set the cell to X
    board[row][col] = 'X'
    print_board(board)

def button_click_o(row, col):
    # Set the cell to O
    board[row][col] = 'O'
    print_board(board)


def initialize_board():
    board = []
    for i in range(3):
        board.append([' ', ' ', ' '])
    return board


def print_board(board):
    for row in board:
        print(row)
    print()


def check_winner(board):
    # Check for horizontal wins
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    # Check for vertical wins
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def check_tie(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def check_game_over(board):
    if check_winner(board):
        print('Winner!')
        return True
    if check_tie(board):
        print('Tie!')
        return True
    return False



App.mainloop()

