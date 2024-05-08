import tkinter.messagebox
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from db_connection import db_con
import os

def login_val():
    """

    :return:
    """
    mysql_conn=db_con_obj.create_db_con('your_db_name','db_password','db_address','db_name')
    data=db_con_obj.execute_mysql_qry(mysql_conn,"SELECT * FROM lib_mngmt.login where id='"+user_name.get()+"' and passwd='"+password.get()+"'")
    mysql_conn.close()
    if data!=[]:
        messagebox.showinfo("Lib Management","Login Successful")
        if data[0][0]== 'username_no':
            lib_home_page_admin()
        else:
            lib_home_page_user()
    else:
        messagebox.showinfo("Login failed", "provide valid id and password")

def clear():
    user_name.set("")
    password.set("")

def lib_home_page_admin():
    root.destroy()
    os.system('admin.py')
    # new_root=Tk()
    # new_root.title("Welcome to the Online Library")
    # new_root.geometry("1500x1000")

def lib_home_page_user():
    root.destroy()
    os.system('user_page.py')
    # new_root=Tk()
    # new_root.title("Welcome to the Online Library")
    # new_root.geometry("1500x1000")

db_con_obj = db_con()
root = Tk()
# root.geometry("400x300")
root.title("Library Management")
root.geometry("1500x1000")

login_img = Image.open("libary.png")
login_img_load = ImageTk.PhotoImage(login_img)
login_bg_img = Label(root,image=login_img_load)
login_bg_img.place(x=0,y=0)

user_name = StringVar()
password = StringVar()
Label(root, text="Please enter login details").pack(pady=10)

Label(root,text="Username").pack(pady=0)
user_name_Entry = Entry(root,textvariable=user_name).pack(pady=5)

Label(root,text="password").pack(pady=0)
passEntry = Entry(root,textvariable=password,show="*").pack(pady=5)
Button(root,text='Login',command=login_val ).pack(pady=5)
Button(root,text='Cancel',command=clear).pack(pady=5)
# Button(root,text='Admin',command=admin_page()).pack(pady=5)

root.mainloop()
