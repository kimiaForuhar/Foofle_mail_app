from tkinter import *
from SQL import Procedures as P


# from GUI import Login


def Signup():
    global pwordE
    global nameE
    global phoneE
    global roots
    labelfont = ('times', 20, 'bold')
    # myfont = ('times', 15, 'bold')
    roots = Tk()
    roots.configure(bg='#DBCEEC')
    roots.geometry("400x500")
    roots.title('Foofle')
    intruction = Label(roots, text='Sign Up Foofle\n', bg='#DBCEEC')
    intruction.place(x=115, y=20)
    intruction.config(font=labelfont)
    nameL = Label(roots, text='Username: ', bg='#DBCEEC')
    pwordL = Label(roots, text='Password: ', bg='#DBCEEC')
    phoneL = Label(roots, text='phone(emergency): ', bg='#DBCEEC')
    nameL.place(x=90, y=80)
    pwordL.place(x=90, y=100)
    phoneL.place(x=90, y=120)
    nameE = Entry(roots)
    pwordE = Entry(roots, show='*')
    phoneE = Entry(roots)
    nameE.place(x=210, y=80)
    pwordE.place(x=210, y=100)
    phoneE.place(x=210, y=120)
    first_name = Label(roots, text="first name:", bg='#DBCEEC')
    first_name.place(x=90, y=140)
    # first_name.config(font=myfont)
    firste = Entry(roots)
    firste.place(x=210, y=140)
    lastname = Label(roots, text="last name:", bg='#DBCEEC')
    lastname.place(x=90, y=160)
    # lastname.config(font=myfont)
    lastnamee = Entry(roots)
    lastnamee.place(x=210, y=160)
    nickname = Label(roots, text="nick name:", bg='#DBCEEC')
    nickname.place(x=90, y=180)
    # nickname.config(font=myfont)
    nick = Entry(roots)
    nick.place(x=210, y=180)
    n_id = Label(roots, text="nationality id:", bg='#DBCEEC')
    n_id.place(x=90, y=200)
    # n_id.config(font=myfont)
    n_ide = Entry(roots)
    n_ide.place(x=210, y=200)
    birthdate = Label(roots, text="birth date:", bg='#DBCEEC')
    birthdate.place(x=90, y=220)
    # birthdate.config(font=myfont)
    birthdatee = Entry(roots)
    birthdatee.place(x=210, y=220)
    phone = Label(roots, text="phone:", bg='#DBCEEC')
    phone.place(x=90, y=240)
    # phone.config(font=myfont)
    phonee = Entry(roots)
    phonee.place(x=210, y=240)
    address = Label(roots, text="address:", bg='#DBCEEC')
    address.place(x=90, y=260)
    # address.config(font=myfont)
    addresse = Text(roots, width=28, height=4)
    addresse.place(x=90, y=280)
    signupButton = Button(roots, text='Sign up', bg='#ffb3fe', command=FSSignup)
    signupButton.place(x=170, y=400)
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