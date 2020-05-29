from tkinter import *
from GUI import SignUp, News
from SQL import Procedures as P


def mynews():
    rootA.destroy()
    News.callnews()


def newUser():
    rootA.destroy()
    SignUp.main()


def Login():
    global nameEL
    global pwordEL
    global rootA, loginB
    labelfont = ('times', 20, 'bold')
    rootA = Tk()
    rootA.configure(bg='#DBCEEC')
    rootA.geometry("400x500")
    rootA.title('Foofle')
    intruction = Label(rootA, text='Login\n', bg='#DBCEEC')
    intruction.place(x=160, y=20)
    intruction.config(font=labelfont)
    nameL = Label(rootA, text='Username: ', bg='#DBCEEC')
    pwordL = Label(rootA, text='Password: ', bg='#DBCEEC')
    nameL.place(x=100, y=80)
    pwordL.place(x=100, y=120)
    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.place(x=170, y=80)
    pwordEL.place(x=170, y=120)
    loginB = Button(rootA, text=' Login ', command=getinput)
    loginB.place(x=170, y=160)
    signuntext = Label(rootA, text="don't have an account?\nsignup now", bg='#DBCEEC')
    signuntext.place(x=130, y=210)
    signupB = Button(rootA, text='sign up', command=newUser)
    signupB.place(x=170, y=250)
    rootA.resizable(0, 1)
    rootA.mainloop()


def getinput():
    un = nameEL.get()
    passw = pwordEL.get()
    if P.userscheckpass(un,passw):
        News.callnews()
        P.AddToLoginTable(un)
    # rootA.destroy()




Login()
