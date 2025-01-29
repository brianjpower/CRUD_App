# This is a sample Python script.
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def gui():
    window = Tk()
    name = Label(text="Employee CRUD App", fg="blue", bg="white", font=("Arial Bold", 12))
    window.geometry("400x300")
    window.title("Employee CRUD App")
    name = Label(text="Employee CRUD App", fg="blue", bg="white", font=("Arial Bold", 12))
    name.pack()
    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
