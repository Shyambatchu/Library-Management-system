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
data=db_con_obj.execute_mysql_qry(mysql_conn,"SELECT * FROM lib_mngmt.book_history")

win = Tk()
win.geometry("1500x1000")
style = ttk.Style()
style.theme_use('clam')

Button(win,text='Home',command=back2_home).pack(pady=15)
# Add a Treeview widget
tree = ttk.Treeview(win, column=("BookID", "BooksName", "IssuedPerson","IssuedDate","ReturnedDate"), show='headings', height=len(data))
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="BookId")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="BooksName")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="IssuedPerson")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="IssuedDate")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="ReturnedDate")

for qry_data in(data):
    tree.insert('', 'end', text="1", values=(qry_data[0], qry_data[1], qry_data[2],qry_data[3],qry_data[4]))
tree.pack()
win.mainloop()
