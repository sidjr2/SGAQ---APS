import tkinter as tk
from tkinter import ttk

class ViewUser(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # -- LABELS -- 
        # Nome
        self.label1 = ttk.Label(self, text='Nome:')
        self.label1.grid(row=0, column=0)
        # Matricula
        self.label2 = ttk.Label(self, text='Matricula:')
        self.label2.grid(row=1, column=0)
        # Tipo
        self.label3 = ttk.Label(self, text='Tipo:')
        self.label3.grid(row=2, column=0)
        # Email
        self.label4 = ttk.Label(self, text='Email:')
        self.label4.grid(row=3, column=0)
        # Telefone
        self.label5 = ttk.Label(self, text='Telefone:')
        self.label5.grid(row=4, column=0)
        # Data de Nascimento
        self.label6 = ttk.Label(self, text='Data Nascimento:')
        self.label6.grid(row=5, column=0)
        #Cidade
        self.labelcidade = ttk.Label(self, text='Cidade:')
        self.labelcidade.grid(row=6, column=0)
        #Senha
        self.labelsenha = ttk.Label(self, text='Senha:')
        self.labelsenha.grid(row=7, column=0)

        # -- WIDGETS -- 
        # Nome
        self.nome_var = tk.StringVar()
        self.nome_entry = ttk.Entry(self, textvariable=self.nome_var, width=30)
        self.nome_entry.grid(row=0, column=1, sticky=tk.NSEW)
        # Matricula
        self.matricula_var = tk.StringVar()
        self.matricula_entry = ttk.Entry(self, textvariable=self.matricula_var, width=30)
        self.matricula_entry.grid(row=1, column=1)
        # Tipo
        self.tipo_var = tk.StringVar()
        self.tipo_entry = ttk.Combobox(self, textvariable=self.tipo_var, width=25)
        self.tipo_entry.grid(row=2, column=1)
        # Email
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=3, column=1)
        # Telefone
        self.telefone_var = tk.StringVar()
        self.telefone_entry = ttk.Entry(self, textvariable=self.telefone_var, width=30)
        self.telefone_entry.grid(row=4, column=1)
        # Data de Nascimento
        self.data_nascimento_var = tk.StringVar()
        self.data_nascimento_var_entry = ttk.Entry(self, textvariable=self.data_nascimento_var, width=30)
        self.data_nascimento_var_entry.grid(row=5, column=1)
        # Cidade
        self.cidade_var = tk.StringVar()
        self.cidade_entry = ttk.Entry(self, textvariable=self.cidade_var, width=30)
        self.cidade_entry.grid(row=6, column=1)
        # Senha
        self.senha_var = tk.StringVar()
        self.senha_entry = ttk.Entry(self, textvariable=self.senha_var, width=30)
        self.senha_entry.grid(row=7, column=1)
        # Cargo
        self.cargo_var = tk.StringVar()
        self.cargo_var_entry = None
          
        # Departamento 
        self.depto_var = tk.StringVar()
        self.depto_var_entry = None
        
        self.last_row = 7

        def option_selected(event):
            if self.cargo_var_entry is not None:
                self.cargo_var_entry.delete(0,'end')
                self.label8.destroy()
                self.cargo_var_entry.destroy()
                self.cargo_var_entry = None
                self.last_row -= 1
            if self.depto_var_entry is not None:
                self.label7.destroy()
                self.depto_var_entry.destroy()
                self.depto_var_entry = None
                self.last_row -= 1
            opcao_selecionada = self.tipo_entry.get()
            match opcao_selecionada:
                case 'Adm':
                    # Departamento
                    if self.depto_var_entry is None:
                        #Label
                        self.label7 = ttk.Label(self, text='Departamento:')
                        self.label7.grid(row=self.last_row+1, column=0)
                        #Widget
                        self.depto_var_entry = ttk.Entry(self, textvariable=self.depto_var, width=30)
                        self.depto_var_entry.grid(row=self.last_row+1, column=1)
                        self.last_row += 1
                    # Cargo
                    if self.cargo_var_entry is None:
                        #Label
                        self.label8 = ttk.Label(self, text='Cargo:')
                        self.label8.grid(row=self.last_row+1, column=0)
                        #Widget
                        self.cargo_var_entry = ttk.Entry(self, textvariable=self.cargo_var, width=30)
                        self.cargo_var_entry['state'] = 'normal'   
                        self.cargo_var_entry.grid(row=self.last_row+1, column=1)
                        self.last_row += 1
                    return 0
                case 'Funcionario':
                    # Departamento
                    if self.depto_var_entry is None:
                        #Label
                        self.label7 = ttk.Label(self, text='Departamento:')
                        self.label7.grid(row=self.last_row+1, column=0)
                        #Widget
                        self.depto_var_entry = ttk.Entry(self, textvariable=self.depto_var, width=30)
                        self.depto_var_entry.grid(row=self.last_row+1, column=1)
                        self.last_row += 1
                    # Cargo
                    if self.cargo_var_entry is None:
                        #Label
                        self.label8 = ttk.Label(self, text='Cargo:')
                        self.label8.grid(row=self.last_row+1, column=0)
                        #Widget
                        self.cargo_var_entry = ttk.Entry(self, textvariable=self.cargo_var, width=30)
                        self.cargo_var_entry['state'] = 'normal'   
                        self.cargo_var_entry.grid(row=self.last_row+1, column=1)
                        self.last_row += 1
                    return 0
                case 'Atletica':
                    # Departamento
                    if self.depto_var_entry is None:
                        #Label
                        self.label7 = ttk.Label(self, text='Departamento:')
                        self.label7.grid(row=self.last_row+1, column=0)
                        #Widget
                        self.depto_var_entry = ttk.Entry(self, textvariable=self.depto_var, width=30)
                        self.depto_var_entry.grid(row=self.last_row+1, column=1)
                        self.last_row += 1
                    # Cargo = Aluno
                    if self.cargo_var_entry is None:
                        #Label
                        self.label8 = ttk.Label(self, text='Cargo:')
                        self.label8.grid(row=self.last_row+1, column=0)
                        #Widget
                        self.cargo_var_entry = ttk.Entry(self, textvariable=self.cargo_var, width=30)
                        self.cargo_var_entry.grid(row=self.last_row+1, column=1)
                        self.cargo_var_entry.delete(0,'end')
                        self.cargo_var_entry.insert(0,'Aluno')
                        self.cargo_var_entry['state'] = 'readonly'
                        self.last_row += 1
                    return 0 
                case 'Aluno':
                    # Sem Cargo
                    if self.cargo_var_entry is not None:
                        self.label8.destroy()
                        self.cargo_var_entry.destroy()
                        self.cargo_var_entry = None
                        self.last_row = self.last_row - 1
                    #Departamento
                    if self.depto_var_entry is None:
                        #Label
                        self.label7 = ttk.Label(self, text='Departamento:')
                        self.label7.grid(row=self.last_row+1, column=0)
                        #Widget
                        self.depto_var_entry = ttk.Entry(self, textvariable=self.depto_var, width=30)
                        self.depto_var_entry.grid(row=self.last_row+1, column=1)
                        self.last_row += 1    
                    return 0
                case 'Comunidade':
                    # Matricula gerada automaticamente
                    # Departamento
                    if self.depto_var_entry is not None:
                        self.label7.destroy()
                        self.depto_var_entry.destroy()
                        self.depto_var_entry = None
                        self.last_row = self.last_row - 1
                    # Cargo
                    if self.cargo_var_entry is None:
                        #Label
                        self.label8 = ttk.Label(self, text='Cargo:')
                        self.label8.grid(row=self.last_row+1, column=0)
                        #Widget
                        self.cargo_var_entry = ttk.Entry(self, textvariable=self.cargo_var, width=30)
                        self.cargo_var_entry['state'] = 'normal'   
                        self.cargo_var_entry.grid(row=self.last_row+1, column=1)
                        self.last_row += 1 
                    return 0
                case _:
                    print("Valor Errado")
                    return
        self.tipo_entry.bind("<<ComboboxSelected>>", option_selected) 


        #Valores do campo
        self.tipo_entry['values'] = ['Adm', 'Funcionario', 'Atletica', 'Aluno', 'Comunidade']
        #Impedir de digitar
        self.tipo_entry['state'] = 'readonly'
    

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=self.last_row+1, column=1, sticky=tk.W)

        # set the controller
        self.controller = None
         
        
    def gera_matricula():
        print('123')

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
            self.controller.save(nome = self.nome_var.get(), matricula = self.matricula_var.get(), tipo = self.tipo_var.get(), email = self.email_var.get(), cargo = self.cargo_var.get(), telefone = self.telefone_var.get(), data_nascimento = self.data_nascimento_var.get(), cidade = self.cidade_var.get(), departamento = self.depto_var.get(), senha = self.senha_var.get())

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

        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

        self.cidade_entry['foreground'] = 'black'
        self.cidade_var.set('')

        self.telefone_entry['foreground'] = 'black'
        self.telefone_var.set('')

        self.senha_entry['foreground'] = 'black'
        self.senha_var.set('')

        self.data_nascimento_var_entry['foreground'] = 'black'
        self.data_nascimento_var.set('')
        if  self.cargo_var_entry is not None:
            self.cargo_var_entry['foreground'] = 'black'
            self.cargo_var.set('')
        if  self.depto_var_entry is not None:
            self.depto_var_entry['foreground'] = 'black'
            self.depto_var.set('')



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
