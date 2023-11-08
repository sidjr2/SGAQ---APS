import re
import tkinter as tk
from model.model import *
from controller.controller import *
from view.view import *
from tkinter import ttk
import mysql.connector

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('SGAQ')

        # Cria o modelo
        model = Model()
        
        #Criando as views
        admview = AdmView(self)
        view = MainView(self, admview)
        # Criando os controladores
        controlleradm = ControllerAdm(model, view)
        controllermenu = ControllerMenu(model, view)
         #Seta os controladores nas views
        admview.set_controller(controlleradm)
        view.set_controller(controllermenu)

        #Desenha a view
        view.grid()
        
        
        
       

if __name__ == '__main__':
    app = App()
    app.mainloop()            