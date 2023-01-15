import random
from tkinter import *

App = Tk()
App.geometry('800x800')

title = Label(App, text='Dice Roller')
title.grid(row=0, column=1, columnspan=2)


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
  roll1 = random.choice(dice)
  roll2 = random.choice(dice)
  roll3 = random.choice(dice)
  roll4 = random.choice(dice)
  return roll1 + roll2 + roll3 + roll4

def roll():
  # Display the dice roll
  dice_roll = roll_dice()
  dice_label = Label(App, text=dice_roll, font=('Helvetica', 260))
  dice_label.grid(row=4, column=0, columnspan=4)


roll_button = Button(App, text='Roll', command=roll)
roll_button.grid(row=1, column=1, columnspan=2)



App.mainloop()

