import tkinter.messagebox
from tkinter import *
from PIL import Image,ImageTk
from db_connection import db_con
import os
from tkinter import messagebox

def back2_home():
    window.destroy()
    os.system('admin.py')

def add_books():
    """

    :return:
    """

    # print(book_record)
    mysql_conn = db_con_obj.create_db_con('')
    result=db_con_obj.execute_mysql_qry(mysql_conn, "select book_id from lib_mngmt.book_status where book_id="+bk_id.get())
    if result !=[]:
        messagebox.showinfo("Add Books", "Duplicate Book ID, kindly provide the unique")
    else:
        inser_record(mysql_conn)

def inser_record(mysql_conn):
    book_record_query="INSERT INTO lib_mngmt.book_status(book_id, books_name, books_count, books_avalibility)VALUES ("+(bk_id.get())+",'"+str(bk_name.get())+"',"+str(bk_tcount.get())+","+str(bk_avail_tcount.get())+")"
   
    db_con_obj.execute_mysql_qry(mysql_conn, book_record_query)
    mysql_conn.commit()
    mysql_conn.close()
    messagebox.showinfo("Add Books", "Record Inserted Successfully")
    window.destroy()
    os.system('admin.py')

db_con_obj = db_con()
window = Tk()
window.title("Welcome to Add books page")
window.geometry("1500x1000")
window.configure(background="black")

Button(window,text='Home',command=back2_home).pack(pady=20)

background_image = PhotoImage(file="img_login.png")
background = Label(window, image=background_image, bd=0)
background.pack()
background.place(relx=0.5, rely=0.5, anchor="sw")

bk_id = StringVar()
bk_name = StringVar()
bk_tcount = StringVar()
bk_avail_tcount = StringVar()

book_id= Label(window,text="Book Id").place(x=30,y=60)
book_id_input_area = Entry(window,textvariable=bk_id,width=30).place(x=170,y=60)
book_name= Label(window,text="Book Name").place(x=30,y=100)
book_name_input_area = Entry(window,textvariable=bk_name,width=30).place(x=170,y=100)
book_TotalCnt= Label(window,text="Book Count").place(x=30,y=150)
book_tcount_input_area = Entry(window,textvariable=bk_tcount,width=30).place(x=170,y=150)
book_availcnt= Label(window,text="BookAvailability").place(x=30,y=200)
book_availcnt_input_area = Entry(window,textvariable=bk_avail_tcount,width=30).place(x=170,y=200)


Button(window,text='AddBooks', height= 3, width=20, fg ='black', bg='orange', command=add_books).place(x=170,y=350)
window.mainloop()


