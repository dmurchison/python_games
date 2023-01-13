from tkinter import *

App = Tk()
App.geometry('300x300')

title = Label(App, text='Tic Tac Toe')
title.grid(row=0, column=0, columnspan=3)


App.mainloop()

