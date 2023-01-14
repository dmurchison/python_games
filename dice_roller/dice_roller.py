import random
from tkinter import *

App = Tk()
App.geometry('300x300')

title = Label(App, text='Dice Roller')
title.grid(row=0, column=0, columnspan=3)


def roll_dice():
  # Roll the dice
  dice = [
    '\u2680',
    '\u2681',
    '\u2682',
    '\u2683',
    '\u2684',
    '\u2685',
    ]
  roll = random.choice(dice)
  return roll

def roll():
  # Display the dice roll
  dice_roll = roll_dice()
  dice_label = Label(App, text=dice_roll, font=('Helvetica', 260))
  dice_label.grid(row=2, column=0, columnspan=3)

roll_button = Button(App, text='Roll', command=roll)
roll_button.grid(row=1, column=0, columnspan=3)



App.mainloop()

