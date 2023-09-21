import tkinter as tk
from tkinter import ttk

class ViewUser(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Nome:')
        self.label.grid(row=0, column=0)

        self.label = ttk.Label(self, text='Matricula:')
        self.label.grid(row=1, column=0)

        self.label = ttk.Label(self, text='Tipo:')
        self.label.grid(row=2, column=0)

        # email entry
        self.nome_var = tk.StringVar()
        self.nome_entry = ttk.Entry(self, textvariable=self.nome_var, width=30)
        self.nome_entry.grid(row=0, column=1, sticky=tk.NSEW)

        self.matricula_var = tk.StringVar()
        self.matricula_entry = ttk.Entry(self, textvariable=self.matricula_var, width=30)
        self.matricula_entry.grid(row=1, column=1)

        self.tipo_var = tk.StringVar()
        self.tipo_entry = ttk.Combobox(self, textvariable=self.tipo_var, width=30)
        self.tipo_entry.grid(row=2, column=1)
        #Valores do campo
        self.tipo_entry['values'] = ['Funcionario', 'Adm', 'Aluno']
        #Impedir de digitar
        self.tipo_entry['state'] = 'readonly'
    

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=3, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.nome_var.get(), self.matricula_var.get(), self.tipo_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.nome_entry['foreground'] = 'black'
        self.nome_var.set('')

        self.matricula_entry['foreground'] = 'black'
        self.matricula_var.set('')
        
        self.tipo_entry['foreground'] = 'black'
        self.tipo_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''  

class ViewQuadra(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Quadra:')
        self.label.grid(row=1, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''  
