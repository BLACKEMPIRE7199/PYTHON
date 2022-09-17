import mysql.connector
from tkinter import messagebox
con = mysql.connector.connect(host="localhost",user="your username",password="your pass",database="your database")


def checker(username,password):
    cur = con.cursor()
    sql = "select * from user where USER=%s and PASSWORD=%s"
    data = (str(username), str(password))
    cur.execute(sql,data)
    h = cur.fetchall()
    lists = []
    for i in h:
        for j in i:
            lists.append(j)

    try:
        if lists[0] == username and lists[1] == password:
            messagebox.showinfo("Sign In",message="Logged in successfully")

    except:
        messagebox.showinfo("Sign In",message="Username and password does not exist")





