from tkinter import *
from PIL import Image,ImageTk
from db_connection import db_con
import os
import tkinter

def book_status():
    window.destroy()
    os.system('Books_availability.py')

def book_srch():
    window.destroy()
    os.system('books.py')

def add_books():
    window.destroy()
    os.system('Add_Books.py')


def user():
    os.system('user.py')

db_con_obj = db_con()
window = Tk()
window.title("Admin Details")
window.geometry("1500x1000")
window.configure(background="black")

background_image = PhotoImage(file="img.png")
background = Label(window, image=background_image, bd=0)
background.pack()

Button(window,text='Books search', height= 1, width=15, fg ='black', bg='orange', command=book_srch).pack(pady=15)
Button(window,text='Add Books', height= 1, width=15, fg ='black', bg='orange',command=add_books).pack(pady=10)
Button(window,text='User info',height= 1, width=15, fg ='black', bg='orange',command=user).pack(pady=10)
Button(window,text='Availability Status',height= 1, width=15, fg ='black', bg='orange',command=book_status).pack(pady=10)


window.mainloop()
