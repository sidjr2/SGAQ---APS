import re
import tkinter as tk
from model.model import *
from controller.controller import *
from view.view import *
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('SGAQ')

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = ViewUser(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()            