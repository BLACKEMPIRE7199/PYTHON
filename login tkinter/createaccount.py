from tkinter import *
from tkinter import messagebox
import mysql.connector
con = mysql.connector.connect(host="localhost",user="your username",password="your password",database="your database name")
def createaccount(username,password):
    cur = con.cursor()
    sql2 = "select * from user where USER=%s and PASSWORD=%s"
    data2 = (str(username), str(password))
    cur.execute(sql2, data2)
    h = cur.fetchall()
    lists1 = []
    for i in h:
        for j in i:
            lists1.append(j)
    try:
        if lists1[0] == username and lists1[1] == password:
            messagebox.showinfo("Sign Up", message="Username and password already exists")

    except:
        pass

    try:
        sql = "insert into user(USER,PASSWORD) values(%s,%s)"
        data = (username, password)
        cur.execute(sql, data)
        con.commit()
        sql1 = "select * from user where USER=%s and PASSWORD=%s"
        data1 = (str(username), str(password))
        cur.execute(sql1, data1)
        h = cur.fetchall()
        lists = []
        for i in h:
            for j in i:
                lists.append(j)
    except:
        messagebox.showinfo("Sign Up",message="username or password already exist")
    try:
        if lists[0] == username and lists[1] == password:
            messagebox.showinfo("Sign Up", message="Signed Up successfully")

    except:
        messagebox.showinfo("Sign Up", message="Username and password already  exist")


