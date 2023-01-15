from tkinter import *
from datetime import datetime


App = Tk()
App.title("Date Calculator")
App.geometry("500x500")

msg = Label(App, text='Enter a date')
msg.grid(row=0, column=0, columnspan=5)

dayL = Label(App, text='Day: ')
dayE = Entry(App, width=2)

monthL = Label(App, text='Month: ')
monthE = Entry(App, width=2)

yearL = Label(App, text='Year: ')
yearE = Entry(App, width=4)

dayL.grid(row=1, column=0)
dayE.grid(row=1, column=1)

monthL.grid(row=2, column=0)
monthE.grid(row=2, column=1)

yearL.grid(row=3, column=0)
yearE.grid(row=3, column=1)


def find_seconds():
  day = int(dayE.get())
  month = int(monthE.get())
  year = int(yearE.get())
  date = datetime(year=year, month=month, day=day)
  
  time_now = datetime.now()
  time_diff = time_now - date
  
  seconds = Label(App, text='Time Ago is '+str(time_diff.total_seconds())+' seconds!')
  seconds.grid(row=5, column=0, columnspan=2)

secondsB = Button(App, text='Find Seconds', command=find_seconds)
secondsB.grid(row=4, column=0)


def find_days():
  day = int(dayE.get())
  month = int(monthE.get())
  year = int(yearE.get())
  date = datetime(year=year, month=month, day=day)
  
  time_now = datetime.now()
  time_diff = time_now - date
  
  days = Label(App, text='Time Ago is '+str(time_diff.days)+' days!')
  days.grid(row=6, column=0, columnspan=2)

daysB = Button(App, text='Find Days', command=find_days)
daysB.grid(row=4, column=1)


def find_months():
  day = int(dayE.get())
  month = int(monthE.get())
  year = int(yearE.get())
  date = datetime(year=year, month=month, day=day)
  
  time_now = datetime.now()
  time_diff = time_now - date
  
  months = Label(App, text='Time Ago is '+str(time_diff.days//30)+' months!')
  months.grid(row=7, column=0, columnspan=2)
  
monthsB = Button(App, text='Find Months', command=find_months)
monthsB.grid(row=4, column=3)


def find_years():
  day = int(dayE.get())
  month = int(monthE.get())
  year = int(yearE.get())
  date = datetime(year=year, month=month, day=day)
  
  time_now = datetime.now()
  time_diff = time_now - date
  
  years = Label(App, text='Time Ago is '+str(time_diff.days//365)+' years!')
  years.grid(row=8, column=0, columnspan=2)
  
yearsB = Button(App, text='Find Years', command=find_years)
yearsB.grid(row=4, column=4)


App.mainloop()

