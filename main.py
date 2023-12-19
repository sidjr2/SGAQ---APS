import tkinter as tk
from view.LoginView import LoginView 
from tkinter import ttk
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('SGAQ')
         # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))
        
        # Criando as views
        login_view = LoginView(self)    
        login_view.draw_view()

if __name__ == '__main__':
    app = App()
    app.mainloop()