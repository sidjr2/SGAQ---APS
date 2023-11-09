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
        viewquadra = ViewQuadra(self)
        viewuser = ViewUser(self)
        view = MainView(self, viewuser, viewquadra)
        view.pack(padx=10, pady=10)
        # create a controller
        controlleruser = ControllerUser(model, viewuser)
        controllerquadra = ControllerQuadra(model,viewquadra)
        
        viewuser.set_controller(controlleruser)
        viewquadra.set_controller(controllerquadra)

class MainView(ttk.Frame):
    def __init__(self, master, user, quadra):
        super().__init__(master)
        self.index = 0

        mainframe = ttk.Frame(master)
        mainframe.pack(padx=10,pady=10,fill='both',expand=1)
        self.framelist = [user, quadra]

        criauser = tk.Button(text='Criar Usuário', command= self.tela_user)
        criauser.pack(padx=10, pady=10)

        criauser = tk.Button(text='Criar Quadra', command= self.tela_quadra)
        criauser.pack(padx=10, pady=10)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
    
    def tela_user(self):
        if self.index == 1:
            self.framelist[1].forget()
        self.framelist[0].tkraise()
        self.framelist[0].pack(padx=10, pady = 10)
        self.index = 0

    def tela_quadra(self):
        if self.index == 0:
            self.framelist[0].forget()
        self.framelist[1].tkraise()
        self.framelist[1].pack(padx=10, pady = 10)
        self.index = 1

if __name__ == '__main__':
    app = App()
    app.mainloop()            