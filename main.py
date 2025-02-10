# This is a sample Python script.
import os
#from gui_components import crud_gui
from gui_components import CrudGUI
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':
    #crud_gui()
    app = CrudGUI("800x470", "Employee CRUD App")
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
