import tkinter as tk
from tkinter import *
from db_connection import db_con
from tkinter import ttk
import os

db_con_obj = db_con()

def back2_home():
    win.destroy()
    os.system('admin.py')

mysql_conn = db_con_obj.create_db_con('')
data=db_con_obj.execute_mysql_qry(mysql_conn,"SELECT * FROM lib_mngmt.user_table")

win = Tk()
win.geometry("1500x1000")
style = ttk.Style()
style.theme_use('clam')

Button(win,text='Home',command=back2_home).pack(pady=15)
# Add a Treeview widget
tree = ttk.Treeview(win, column=("REGNO","Name","DEGREE","BRANCH","NO.OF_BOOKS_TAKEN","FINE"), show='headings', height=len(data))
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="REGNO")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Name")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="DEGREE")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="BRANCH")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="NO.OF_BOOKS_TAKEN")
tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="FINE")


for qry_data in(data):
    tree.insert('', 'end', text="1", values=(qry_data[0], qry_data[1], qry_data[2],qry_data[3],qry_data[4],qry_data[5]))
tree.pack()
win.mainloop()

