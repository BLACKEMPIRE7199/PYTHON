from tkinter import *
from tkinter import messagebox
from confirm import checker
from createaccount import createaccount
window = Tk()
appwidth = 1080
appheight = 720
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth/2) - (appwidth/2)
y = (screenheight/2) - (appheight/2)
window.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')
window.title("SIGN IN PAGE")
window.resizable(False,False)


svg1 = PhotoImage(file="assets//Company-pana.png")
svgl1 = Label(window, image = svg1).place(x = 3, y = 50)
svg2 = PhotoImage(file="assets//circle.png")
svgl2 = Label(window, image = svg2).place(x = 610, y = 45)
text = Label(window,text="Sign In",fg="black",bg="white",font=("Microsoft JhengHei UI",18))
text.place(x=785,y=85)
#entry box
def focus_inU(event):
    username.delete(0,END)
    username.config(fg="black")

def focus_outU(event):
    if username.get() == "":
        username.insert(0, "USERNAME")
    username.config(fg="#939597")

def focus_inP(event):
    password.delete(0, END)
    password.config(fg="black")

def focus_outP(event):
    if password.get() == "":
       password.insert(0, "PASSWORD")
    password.config(fg="#939597")

username = Entry(window,width=35,border=0,font=("consolas",14),borderwidth=0,fg="#939597")
username.insert(0,"USERNAME")
username.place(x=640,y=235)
username.bind("<FocusIn>",focus_inU)
username.bind("<FocusOut>",focus_outU)
username_line=Frame(window,width=380,height=2,bg="black",border=0).place(x=640,y=260)



password = Entry(window,width=32,border=0,font=("consolas",14),borderwidth=0,fg="#939597")
password.insert(0, "PASSWORD")
password.place(x=640, y=350)
password.bind("<FocusIn>", focus_inP)
password.bind("<FocusOut>", focus_outP)
password_line=Frame(window,width=380,height=2,bg="black",border=0).place(x=640,y=375)

def confirm():
    user = username.get()
    passwd = password.get()
    username.delete(0, END)
    password.delete(0, END)
    checker(user, passwd)
def forget():

    window2 = Toplevel()
    window2.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')
    window2.title("SIGN UP PAGE")
    window2.resizable(False, False)
    svg1top = PhotoImage(file="assets//In the office-pana.png")
    svgl1top = Label(window2, image=svg1top).place(x = 3, y = 50)
    svg2top = PhotoImage(file="assets//hex.png")
    svgl2top = Label(window2, image=svg2top).place(x = 600, y = 45)
    texttop = Label(window2, text="Sign Up", fg="black", bg="white", font=("Microsoft JhengHei UI", 18))
    texttop.place(x=785, y=85)

    def focus_inU(event):
        username2.delete(0, END)
        username2.config(fg="black")

    def focus_outU(event):
        if username2.get() == "":
            username2.insert(0, "USERNAME")
        username2.config(fg="#939597")

    def focus_inP(event):
        password2.delete(0, END)
        password2.config(fg="black")

    def focus_outP(event):
        if password2.get() == "":
            password2.insert(0, "PASSWORD")
        password2.config(fg="#939597")

    def focus_inPc(event):
        passwordc.delete(0, END)
        passwordc.config(fg="black")

    def focus_outPc(event):
        if passwordc.get() == "":
            passwordc.insert(0, "CONFIRM PASSWORD")
        passwordc.config(fg="#939597")

    username2 = Entry(window2, width=35, border=0, font=("consolas", 14), borderwidth=0, fg="#939597")
    username2.insert(0, "USERNAME")
    username2.place(x=640, y=235)
    username2.bind("<FocusIn>", focus_inU)
    username2.bind("<FocusOut>", focus_outU)
    username_line2 = Frame(window2, width=380, height=2, bg="black", border=0).place(x=640, y=260)

    password2 = Entry(window2, width=32, border=0, font=("consolas", 14), borderwidth=0, fg="#939597")
    password2.insert(0, "PASSWORD")
    password2.place(x=640, y=335)
    password2.bind("<FocusIn>", focus_inP)
    password2.bind("<FocusOut>", focus_outP)
    password_line2 = Frame(window2, width=380, height=2, bg="black", border=0).place(x=640, y=360)


    passwordc = Entry(window2, width=32, border=0, font=("consolas", 14), borderwidth=0, fg="#939597")
    passwordc.insert(0, "CONFIRM PASSWORD")
    passwordc.place(x=640, y=435)
    passwordc.bind("<FocusIn>", focus_inPc)
    passwordc.bind("<FocusOut>", focus_outPc)
    password_line2c= Frame(window2, width=380, height=2, bg="black", border=0).place(x=640, y=460)

    def destroy():
        window2.forget(window2)


    def confirm():
        user = username2.get()
        passwd = password2.get()
        cpasswd = passwordc.get()
        if passwd == cpasswd:
            username2.delete(0, END)
            password2.delete(0, END)
            createaccount(user, passwd)
        else:
            messagebox.showinfo("Sign Up",message="Password does not match with confirm password")
            passwordc.delete(0, END)

    create = Label(window2, text="Already have an account", font=("Helvetica", 14), border=0, bg="white").place(x=680, y=620)
    signin = Button(window2, text="Sign In", font=("Didot", 13), border=0, bg="white", fg="#662622",
                    activebackground="white", activeforeground="#ba3a30", command=destroy).place(x=930, y=618)

    confirm = Button(window2, text="Confirm", font=("Arial", 12), border=0, fg="white", bg="#cc4735", width=20, height=2,
                     command=confirm).place(x=740, y=520)


    window2.mainloop()



account = Label(window,text="Not an existing user",font=("Helvetica",14),border=0,bg="white",fg="black").place(x=735,y=550)

create = Label(window,text="Create an account",font=("Helvetica",14),border=0,bg="white").place(x=680,y=620)
signup = Button(window,text="Sign Up",font=("Didot",13),border=0,bg="white",fg="#662622",activebackground="white",activeforeground="#ba3a30",command=forget).place(x=880,y=618)



confirm = Button(window,text="Confirm",font=("Arial",12),border=0,fg="white",bg="#cc4735",width=20,height=2,command=confirm).place(x=730,y=440)

window.mainloop()