from tkinter import *


def error(e):
    labelfont = ('times', 15, 'bold')
    rootA = Tk()
    rootA.configure(bg='#DBCEEC')
    rootA.geometry("700x200")
    rootA.title('Foofle')
    intruction = Label(rootA, text=e, bg='#DBCEEC')
    intruction.place(x=100,y=50)
    intruction.config(font=labelfont)