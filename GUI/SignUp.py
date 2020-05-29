from tkinter import *
from SQL import Procedures as P


# from GUI import Login


def Signup():
    global pwordE
    global nameE
    global phoneE
    global roots
    labelfont = ('times', 20, 'bold')
    roots = Tk()
    roots.configure(bg='#DBCEEC')
    roots.geometry("400x500")
    roots.title('Foofle')
    intruction = Label(roots, text='Sign Up Foofle\n', bg='#DBCEEC')
    intruction.place(x=115, y=20)
    intruction.config(font=labelfont)
    nameL = Label(roots, text='Username: ', bg='#DBCEEC')
    pwordL = Label(roots, text='Password: ', bg='#DBCEEC')
    phoneL = Label(roots, text='phone: ', bg='#DBCEEC')
    nameL.place(x=100, y=80)
    pwordL.place(x=100, y=120)
    phoneL.place(x=100, y=160)
    nameE = Entry(roots)
    pwordE = Entry(roots, show='*')
    phoneE = Entry(roots)
    nameE.place(x=200, y=80)
    pwordE.place(x=200, y=120)
    phoneE.place(x=200, y=160)
    signupButton = Button(roots, text='Sign up', bg='#ffb3fe', command=FSSignup)
    signupButton.place(x=170, y=220)
    roots.resizable(0, 1)
    roots.mainloop()


def FSSignup():
    un = nameE.get()
    passw = pwordE.get()
    phone = phoneE.get()
    P.addNewUser(un, passw, phone)
    roots.destroy()
    # Login.calllogin()


def main():
    Signup()