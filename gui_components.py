# This is a module containing various gui window elements and their associated action calls
from tkinter import *
from tkinter import messagebox
from utilities import show
from sql_database_ops import Crud_sql_ops
#from sql_database_ops import insertData, removeData, getData, updateData, resetFields



class CrudGUI:
    def __init__(self,geom, windowTitle):
        #Initialise the main window
        self.window = Tk()
        self.window.geometry(geom)
        self.window.title(windowTitle)

        #Now define the main properties
        self.enterID = None
        self.enterName = None
        self.enterDept = None
        self.listBox = None
        self.enter_data()
        self.create_listbox()
        self.emp_crud_ops = Crud_sql_ops(self.enterID, self.enterName, self.enterDept, self.listBox)
        self.create_buttons()
        self.create_labels()




    def create_buttons(self):
        insertBtn = Button(self.window, text="Insert", font=("Sans", 12), bg="white", command=self.emp_crud_ops.insertData)
        insertBtn.place(x=20, y=160)
        updateBtn = Button(self.window, text="Update", font=("Sans", 12), bg="white",command=self.emp_crud_ops.updateData)
        updateBtn.place(x=80, y=160)
        fetchBtn = Button(self.window, text="Fetch", font=("Sans", 12), bg="white",command=self.emp_crud_ops.getData)
        fetchBtn.place(x=150, y=160)
        deleteBtn = Button(self.window, text="Delete", font=("Sans", 12), bg="white",command=self.emp_crud_ops.removeData)
        deleteBtn.place(x=210, y=160)
        resetBtn = Button(self.window, text="Reset", font=("Sans", 12), bg="white",command=self.emp_crud_ops.resetFields)
        resetBtn.place(x=20, y=210)

    def create_labels(self):
        empID = Label(self.window, text="Employee ID", font=("Serif", 12))
        empID.place(x=20, y=30)
        empName = Label(self.window, text="Employee Name", font=("Serif", 12))
        empName.place(x=20, y=60)
        empDept = Label(self.window, text="Employee Dept", font=("Serif", 12))
        empDept.place(x=20, y=90)

    def create_listbox(self):
        """
        Add a listbox to display employee data.
        """
        self.listBox = Listbox(self.window)
        self.listBox.place(x=330, y=30, width=300)
        # Call the utility `show` to populate initial data
        show(self.listBox)
    def enter_data(self):
        self.enterID = Entry(self.window)
        self.enterID.place(x=170, y=30)
        self.enterName = Entry(self.window)
        self.enterName.place(x=170, y=60)
        self.enterDept = Entry(self.window)
        self.enterDept.place(x=170, y=90)


    def run(self):
        self.window.mainloop()

