import tkinter as tk
from tkinter import ttk
import copy


# Menu principal

class MainView(ttk.Frame):
    def __init__(self, master, adm, geral):
        super().__init__(master)
        self.index = 0
        self.mainframe = ttk.Frame(master)
        self.mainframe.grid(padx=10, pady=10)

        self.framelist = [adm, geral]
        labels = ['Matricula', 'Senha']
        self.label = []
        self.entry = 2
        self.row = 0
        self.column = 0

        for i in labels:
            self.label.append(tk.Label(text=f'{i}'))
            self.label[self.row].grid(row=self.row, column=self.column)
            self.row += 1

        self.row = 0
        self.column = 1

        self.matricula_var = tk.StringVar()
        self.textomatricula = tk.Entry(textvariable=self.matricula_var)
        self.textomatricula.grid(row=self.row, column=self.column)
        self.row += 1

        self.senha_var = tk.StringVar()
        self.textosenha = tk.Entry(textvariable=self.senha_var, show='*')
        self.textosenha.grid(row=self.row, column=self.column)
        self.row += 2

        self.botaologin = tk.Button(text='Login', command=self.realiza_login)
        self.botaologin.grid(row=self.row, column=self.column)
        self.row += 2

        self.botaosuporte = tk.Button(text='Contatar Suporte', command=self.chama_suporte)
        self.botaosuporte.grid(row=self.row, column=self.column)
        self.row += 1

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=self.row, column=self.column)

    def chama_suporte(self):
        self.mensagem('Entre em contato com o email: XXX@XXX.com')

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def realiza_login(self):
        if self.controller:
            self.controller.login(matricula=self.matricula_var.get(), senha=self.senha_var.get())

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

    def show_login(self, tipo):
        # Sumindo com widgets de login
        self.textomatricula.grid_forget()
        self.label[0].grid_forget()
        self.textosenha.grid_forget()
        self.label[1].grid_forget()
        self.botaologin.grid_forget()
        self.botaosuporte.grid_forget()
        # Chamando view de adm
        if tipo == 'Adm':
            self.framelist[0].on_login(self.textomatricula.get())
        else:
        #Chamando view de geral
            self.framelist[1].on_login(self.textomatricula.get())
        

        self.index = 1

    def mensagem(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

    def show_error(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''

    # Visão do usuário


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
        # Cidade
        self.labelcidade = ttk.Label(self, text='Cidade:')
        self.labelcidade.grid(row=6, column=0)
        # Senha
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
                self.cargo_var_entry.delete(0, 'end')
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
                        # Label
                        self.label7 = ttk.Label(self, text='Departamento:')
                        self.label7.grid(row=self.last_row + 1, column=0)
                        # Widget
                        self.depto_var_entry = ttk.Entry(self, textvariable=self.depto_var, width=30)
                        self.depto_var_entry.grid(row=self.last_row + 1, column=1)
                        self.last_row += 1
                    # Cargo
                    if self.cargo_var_entry is None:
                        # Label
                        self.label8 = ttk.Label(self, text='Cargo:')
                        self.label8.grid(row=self.last_row + 1, column=0)
                        # Widget
                        self.cargo_var_entry = ttk.Entry(self, textvariable=self.cargo_var, width=30)
                        self.cargo_var_entry['state'] = 'normal'
                        self.cargo_var_entry.grid(row=self.last_row + 1, column=1)
                        self.last_row += 1
                    return 0
                case 'Funcionario':
                    # Departamento
                    if self.depto_var_entry is None:
                        # Label
                        self.label7 = ttk.Label(self, text='Departamento:')
                        self.label7.grid(row=self.last_row + 1, column=0)
                        # Widget
                        self.depto_var_entry = ttk.Entry(self, textvariable=self.depto_var, width=30)
                        self.depto_var_entry.grid(row=self.last_row + 1, column=1)
                        self.last_row += 1
                    # Cargo
                    if self.cargo_var_entry is None:
                        # Label
                        self.label8 = ttk.Label(self, text='Cargo:')
                        self.label8.grid(row=self.last_row + 1, column=0)
                        # Widget
                        self.cargo_var_entry = ttk.Entry(self, textvariable=self.cargo_var, width=30)
                        self.cargo_var_entry['state'] = 'normal'
                        self.cargo_var_entry.grid(row=self.last_row + 1, column=1)
                        self.last_row += 1
                    return 0
                case 'Atletica':
                    # Departamento
                    if self.depto_var_entry is None:
                        # Label
                        self.label7 = ttk.Label(self, text='Departamento:')
                        self.label7.grid(row=self.last_row + 1, column=0)
                        # Widget
                        self.depto_var_entry = ttk.Entry(self, textvariable=self.depto_var, width=30)
                        self.depto_var_entry.grid(row=self.last_row + 1, column=1)
                        self.last_row += 1
                    # Cargo = Aluno
                    if self.cargo_var_entry is None:
                        # Label
                        self.label8 = ttk.Label(self, text='Cargo:')
                        self.label8.grid(row=self.last_row + 1, column=0)
                        # Widget
                        self.cargo_var_entry = ttk.Entry(self, textvariable=self.cargo_var, width=30)
                        self.cargo_var_entry.grid(row=self.last_row + 1, column=1)
                        self.cargo_var_entry.delete(0, 'end')
                        self.cargo_var_entry.insert(0, 'Aluno')
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
                    # Departamento
                    if self.depto_var_entry is None:
                        # Label
                        self.label7 = ttk.Label(self, text='Departamento:')
                        self.label7.grid(row=self.last_row + 1, column=0)
                        # Widget
                        self.depto_var_entry = ttk.Entry(self, textvariable=self.depto_var, width=30)
                        self.depto_var_entry.grid(row=self.last_row + 1, column=1)
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
                        # Label
                        self.label8 = ttk.Label(self, text='Cargo:')
                        self.label8.grid(row=self.last_row + 1, column=0)
                        # Widget
                        self.cargo_var_entry = ttk.Entry(self, textvariable=self.cargo_var, width=30)
                        self.cargo_var_entry['state'] = 'normal'
                        self.cargo_var_entry.grid(row=self.last_row + 1, column=1)
                        self.last_row += 1
                    return 0
                case _:
                    print("Valor Errado")
                    return

        self.tipo_entry.bind("<<ComboboxSelected>>", option_selected)

        # Valores do campo
        self.tipo_entry['values'] = ['Adm', 'Funcionario', 'Atletica', 'Aluno', 'Comunidade']
        # Impedir de digitar
        self.tipo_entry['state'] = 'readonly'

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=0, column=2, sticky=tk.W)

        # set the controller
        self.controller = None

    def gera_matricula(self):
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
            self.controller.saveuser(nome=self.nome_var.get(), matricula=self.matricula_var.get(),
                                     tipo=self.tipo_var.get(), email=self.email_var.get(), cargo=self.cargo_var.get(),
                                     telefone=self.telefone_var.get(), data_nascimento=self.data_nascimento_var.get(),
                                     cidade=self.cidade_var.get(), departamento=self.depto_var.get(),
                                     senha=self.senha_var.get())

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
        if self.cargo_var_entry is not None:
            self.cargo_var_entry['foreground'] = 'black'
            self.cargo_var.set('')
        if self.depto_var_entry is not None:
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
        # Dicionario de posiçoes de coluna
        self.griddict = {'nome': 1, 'local': 2, 'capacidade': 3, 'horario_disp': 4, 'horario_limp': 5, 'last': 6}
        nome = self.griddict['nome']
        local = self.griddict['local']
        capacidade = self.griddict['capacidade']
        horario_disp = self.griddict['horario_disp']
        horario_limp = self.griddict['horario_limp']
        last = self.griddict['last']

        # Labels
        self.labelnome = ttk.Label(self, text='Nome da Quadra:')
        self.labelnome.grid(row=nome, column=0)
        self.labelnome = ttk.Label(self, text='Local:')
        self.labelnome.grid(row=local, column=0)
        self.labelnome = ttk.Label(self, text='Capacidade:')
        self.labelnome.grid(row=capacidade, column=0)
        self.labelnome = ttk.Label(self, text='Horario Disponivel:')
        self.labelnome.grid(row=horario_disp, column=0)
        self.labelnome = ttk.Label(self, text='Horario de Limpeza:')
        self.labelnome.grid(row=horario_limp, column=0)

        # Nome
        self.nome_var = tk.StringVar()
        self.nome_entry = ttk.Entry(self, textvariable=self.nome_var, width=30)
        self.nome_entry.grid(row=nome, column=1)
        # Local
        self.local_var = tk.StringVar()
        self.local_entry = ttk.Entry(self, textvariable=self.local_var, width=30)
        self.local_entry.grid(row=local, column=1)
        # Capacidade
        self.capacidade_var = tk.StringVar()
        self.capacidade_entry = ttk.Entry(self, textvariable=self.capacidade_var, width=30)
        self.capacidade_entry.grid(row=capacidade, column=1)
        # Horario Disponivel
        self.horario_disp_var = tk.StringVar()
        self.horario_disp_entry = ttk.Entry(self, textvariable=self.horario_disp_var, width=30)
        self.horario_disp_entry.grid(row=horario_disp, column=1)
        # Horario Limpeza
        self.horario_limp_var = tk.StringVar()
        self.horario_limp_entry = ttk.Entry(self, textvariable=self.horario_limp_var, width=30)
        self.horario_limp_entry.grid(row=horario_limp, column=1)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # Mensagem (Acerto ou erro)
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=last, column=1, sticky=tk.W)

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
            self.controller.savequadra(nome=self.nome_var.get(), local=self.local_var.get(),
                                       capacidade=self.capacidade_var.get(), horario_limp=self.horario_limp_var.get(),
                                       horario_disp=self.horario_disp_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # Resetar formulario

        # Nome
        self.nome_entry['foreground'] = 'black'
        self.nome_var.set('')
        # Local
        self.local_entry['foreground'] = 'black'
        self.local_var.set('')
        # Capacidade
        self.capacidade_entry['foreground'] = 'black'
        self.capacidade_var.set('')
        # Horario Disponivel
        self.horario_disp_entry['foreground'] = 'black'
        self.horario_disp_var.set('')
        # Horario Limpeza
        self.horario_limp_entry['foreground'] = 'black'
        self.horario_limp_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''


class GerenciaUser(ttk.Frame):
    # Pegar os usuarios!!! nome e matricula
    def __init__(self, parent):
        super().__init__(parent)
        self.nome = None
        self.label6 = None
        self.labelcidade = None
        self.called = False
        self.deletebtns = []
        self.editbtns = []
        self.labelnome = []
        self.labelmatricula = []

    def deleteuser(self, user, index):
        self.controller.deleteuser(user)
        self.deletebtns[index].grid_forget()
        self.editbtns[index].grid_forget()
        self.labelnome[index].grid_forget()
        self.labelmatricula[index].grid_forget()

    def deletewidget(self, widget):
        for i in widget:
            i.grid_forget()

    def raisewidget(widget, row, column):
        for i in widget:
            i.grid(row=row, column=column, sticky=tk.NS)

    def deletewidgets(self, widget):
        for i in range(len(widget)):
            widget[i].grid_forget()

    def raisewidgets(self, widget, column):
        for i in range(len(widget)):
            widget[i].grid(row=i + 1, column=column, sticky=tk.NS)

    def drawviewedit(self, user):

        def onsaveclick():
            alteracoes = [self.nome_var, self.matricula_var, self.tipo_var, self.email_var, self.telefone_var,
                          self.data_nascimento_var, self.cidade_var, self.senha_var, self.cargo_var, self.depto_var]
            self.controller.edituser(user, alteracoes)

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
        # Cidade
        self.labelcidade = ttk.Label(self, text='Cidade:')
        self.labelcidade.grid(row=6, column=0)
        # Senha
        self.labelsenha = ttk.Label(self, text='Senha:')
        self.labelsenha.grid(row=7, column=0)
        # Cargo
        self.labelcargo = ttk.Label(self, text='Cargo:')
        self.labelcargo.grid(row=8, column=0)
        # Departamento
        self.labeldepto = ttk.Label(self, text='Departamento:')
        self.labeldepto.grid(row=9, column=0)

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
        # Valores do campo
        self.tipo_entry['values'] = ['Adm', 'Funcionario', 'Atletica', 'Aluno', 'Comunidade']
        # Impedir de digitar
        self.tipo_entry['state'] = 'readonly'
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
        self.cargo_var = ttk.Entry(self, textvariable=self.cargo_var, width=30)
        self.cargo_var.grid(row=8, column=1)
        # Departamento 
        self.depto_var = tk.StringVar()
        self.depto_var = ttk.Entry(self, textvariable=self.depto_var, width=30)
        self.depto_var.grid(row=9, column=1)

        self.save_button = ttk.Button(self, text='Save', command=onsaveclick)
        self.save_button.grid(row=1, column=2, padx=10)

    def edituser(self, user, index):
        list = [self.deletebtns, self.editbtns, self.labelnome, self.labelmatricula]
        list2 = [self.nome, self.matricula]
        for i in list:
            self.deletewidgets(i)
            self.deletewidget(list2)
        self.drawviewedit(user)

        # Reconstroi

    def mostrausers(self):
        usuarios = self.controller.retornauser()
        self.nome = ttk.Label(self, text='Nome:')
        self.matricula = ttk.Label(self, text='Matricula:')
        self.nome.grid(row=0, column=0, sticky=tk.EW)
        self.matricula.grid(row=0, column=1, sticky=tk.EW)
        row = 1
        index = 0

        if not self.called:
            for x in usuarios:
                self.deletebtns.append(
                    ttk.Button(self, text='Delete', command=lambda x=x, index=index: self.deleteuser(x[1], index)))
                self.editbtns.append(
                    ttk.Button(self, text='Edit', command=lambda x=x, index=index: self.edituser(x[1], index)))

                self.labelnome.append(ttk.Label(self, text=f'{x[0]}'))
                self.labelmatricula.append(ttk.Label(self, text=f'{x[1]}'))

                self.labelnome[index].grid(row=row, column=0, sticky=tk.NS)
                self.labelmatricula[index].grid(row=row, column=1, sticky=tk.NS)

                self.editbtns[index].grid(row=row, column=2, sticky=tk.NS)
                self.deletebtns[index].grid(row=row, column=3, sticky=tk.NS)
                index += 1
                row += 1
        self.called = True

    def set_controller(self, controller):
        self.controller = controller


class GerenciaQuadra(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.called = False
        self.deletebtns = []
        self.editbtns = []
        self.labelnome = []
        self.labelmatricula = []

    def deletequadra(self, quadra, index):
        self.controller.deletequadra(quadra)
        self.deletebtns[index].grid_forget()
        self.editbtns[index].grid_forget()
        self.labelnome[index].grid_forget()
        self.labelmatricula[index].grid_forget()

    def deletewidget(self, widget):
        for i in widget:
            i.grid_forget()

    def raisewidget(widget, row, column):
        for i in widget:
            i.grid(row=row, column=column, sticky=tk.NS)

    def deletewidgets(self, widget):
        for i in range(len(widget)):
            widget[i].grid_forget()

    def raisewidgets(self, widget, column):
        for i in range(len(widget)):
            widget[i].grid(row=i + 1, column=column, sticky=tk.NS)

    def drawviewedit(self, quadra):

        def onsaveclick():
            alteracoes = [self.nome_var, self.local_var, self.capacidade_var, self.horario_disp_var,
                          self.horario_limp_var]
            self.controller.editquadra(quadra, alteracoes)
        # Dicionario de posiçoes de coluna
        self.griddict = {'nome': 1, 'local': 2, 'capacidade': 3, 'horario_disp': 4, 'horario_limp': 5, 'last': 6}
        nome = self.griddict['nome']
        local = self.griddict['local']
        capacidade = self.griddict['capacidade']
        horario_disp = self.griddict['horario_disp']
        horario_limp = self.griddict['horario_limp']
        last = self.griddict['last']
        # Labels
        self.labelnome = ttk.Label(self, text='Nome da Quadra:')
        self.labelnome.grid(row=nome, column=0)
        self.labelnome = ttk.Label(self, text='Local:')
        self.labelnome.grid(row=local, column=0)
        self.labelnome = ttk.Label(self, text='Capacidade:')
        self.labelnome.grid(row=capacidade, column=0)
        self.labelnome = ttk.Label(self, text='Horario Disponivel:')
        self.labelnome.grid(row=horario_disp, column=0)
        self.labelnome = ttk.Label(self, text='Horario de Limpeza:')
        self.labelnome.grid(row=horario_limp, column=0)

        # Nome
        self.nome_var = tk.StringVar()
        self.nome_entry = ttk.Entry(self, textvariable=self.nome_var, width=30)
        self.nome_entry.grid(row=nome, column=1)
        # Local
        self.local_var = tk.StringVar()
        self.local_entry = ttk.Entry(self, textvariable=self.local_var, width=30)
        self.local_entry.grid(row=local, column=1)
        # Capacidade
        self.capacidade_var = tk.StringVar()
        self.capacidade_entry = ttk.Entry(self, textvariable=self.capacidade_var, width=30)
        self.capacidade_entry.grid(row=capacidade, column=1)
        # Horario Disponivel
        self.horario_disp_var = tk.StringVar()
        self.horario_disp_entry = ttk.Entry(self, textvariable=self.horario_disp_var, width=30)
        self.horario_disp_entry.grid(row=horario_disp, column=1)
        # Horario Limpeza
        self.horario_limp_var = tk.StringVar()
        self.horario_limp_entry = ttk.Entry(self, textvariable=self.horario_limp_var, width=30)
        self.horario_limp_entry.grid(row=horario_limp, column=1)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=onsaveclick)
        self.save_button.grid(row=1, column=3, padx=10)



    def editquadra(self, quadra, index):
        list = [self.deletebtns, self.editbtns, self.labelnome, self.labelmatricula]
        list2 = [self.nome, self.matricula]
        for i in list:
            self.deletewidgets(i)
            self.deletewidget(list2)
        self.drawviewedit(quadra)

    def mostraquadra(self):
        usuarios = self.controller.retornaquadra()
        self.nome = ttk.Label(self, text='Nome:')
        self.matricula = ttk.Label(self, text='Local:')
        self.nome.grid(row=0, column=0, sticky=tk.EW)
        self.matricula.grid(row=0, column=1, sticky=tk.EW)
        row = 1
        index = 0

        if not self.called:
            for x in usuarios:
                self.deletebtns.append(
                    ttk.Button(self, text='Delete', command=lambda x=x, index=index: self.deletequadra(x[0], index)))
                self.editbtns.append(
                    ttk.Button(self, text='Edit', command=lambda x=x, index=index: self.editquadra(x[0], index)))

                self.labelnome.append(ttk.Label(self, text=f'{x[1]}'))
                self.labelmatricula.append(ttk.Label(self, text=f'{x[2]}'))

                self.labelnome[index].grid(row=row, column=0, sticky=tk.NS)
                self.labelmatricula[index].grid(row=row, column=1, sticky=tk.NS)

                self.editbtns[index].grid(row=row, column=2, sticky=tk.NS)
                self.deletebtns[index].grid(row=row, column=3, sticky=tk.NS)
                index += 1
                row += 1
        self.called = True

    def set_controller(self, controller):
        self.controller = controller


class AdmView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Criar Usuario
        self.controller = None
        user = ViewUser(parent=parent)
        # Criar Quadra
        quadra = ViewQuadra(parent=parent)
        # Gerenciar Usuario
        gerenciauser = GerenciaUser(parent=parent)
        gerenciaquadra = GerenciaQuadra(parent=parent)
        self.framelist = [user, quadra, gerenciauser, gerenciaquadra]

        self.criauser = tk.Button(text='Criar Usuário', command=self.tela_user)
        self.criaquadra = tk.Button(text='Criar Quadra', command=self.tela_quadra)
        self.gerenciauser = tk.Button(text='Gerenciar Usuario', command=self.tela_gerenciamentouser)
        self.gerenciaquadra = tk.Button(text='Gerenciar Quadra', command=self.tela_gerenciamentoquadra)
        self.index = -1

    def tela_user(self):
        if self.index != 0:
            for i in range(len(self.framelist)):
                self.framelist[i].grid_forget()
        self.framelist[0].tkraise()
        self.framelist[0].grid(row=1, column=0, pady=20)
        self.index = 0

    def tela_quadra(self):
        if self.index != 1:
            for i in range(len(self.framelist)):
                self.framelist[i].grid_forget()
        self.framelist[1].tkraise()
        self.framelist[1].grid(row=1, column=1, pady=20)
        self.index = 1

    def tela_gerenciamentouser(self):
        if self.index != 2:
            for i in range(len(self.framelist)):
                self.framelist[i].grid_forget()
        self.framelist[2].mostrausers()
        self.framelist[2].tkraise()
        self.framelist[2].grid(row=1, column=2, pady=20)
        self.index = 2

    def tela_gerenciamentoquadra(self):
        if self.index != 3:
            for i in range(len(self.framelist)):
                self.framelist[i].grid_forget()
        self.framelist[3].mostraquadra()
        self.framelist[3].tkraise()
        self.framelist[3].grid(row=1, column=3, pady=20)
        self.index = 3

    def on_login(self, matricula):
        self.matricula = matricula
        self.gerenciaquadra.grid(row=0, column=3, sticky=tk.EW)
        self.gerenciauser.grid(row=0, column=2, sticky=tk.EW)
        self.criaquadra.grid(row=0, column=1, sticky=tk.EW)
        self.criauser.grid(row=0, column=0, sticky=tk.EW)

    # Gerenciar Reserva
    # reserva = ViewReserva()
    # Registrar punição
    # punicao = ViewPunicao
    # Analisar recurso
    # Visualizar estatisticas
    # Gerenciar Usuarios
    # gerenciauser = ViewUserGerencia()
    # Gerenciar Equipamentos
    # gerenciaequip = ViewEquipamento()

    # Controlador
    def set_controller(self, controller):
        self.controller = controller
        for x in self.framelist:
            x.set_controller(controller)


class GeralView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Adicione os widgets para a criação e visualização de reserva de quadra aqui
        self.criar_reserva_button = ttk.Button(parent, text='Criar Reserva', command=self.criar_reserva)
        self.visualizar_reserva_button = ttk.Button(parent, text='Visualizar Reserva', command=self.visualizar_reserva)
        self.registrar_presença_button = ttk.Button(parent, text='Registrar Presença', command = self.registrar_presença)
        
        

    def on_login(self, matricula):
        self.matricula = matricula
        self.criar_reserva_button.grid(row=0, column=0)
        self.visualizar_reserva_button.grid(row=0, column=1)
        self.registrar_presença_button.grid(row=0, column=2)

    def criar_reserva(self):
        nova_janela = tk.Toplevel(self)
        nova_janela.title('Criar Reserva')
    # Adicione os widgets para a criação de reserva aqui
        label_quadras = ttk.Label(nova_janela, text='Selecione a Quadra:')
        label_quadras.grid(row=0, column=0, padx=10, pady=10)

        self.message_label = ttk.Label(nova_janela, text='', foreground='red')
        self.message_label.grid(row=2, column=2, sticky=tk.W)

        # Exemplo de ComboBox com quadras (substitua com sua lista de quadras)
        quadras = self.controller.fetch_quadras()
        self.quadras_var = tk.StringVar()
        select_quadras = ttk.Combobox(nova_janela,textvariable=self.quadras_var, values=quadras)
        select_quadras.grid(row=0, column=1, padx=10, pady=10)

        #Data inicio
        label_data = ttk.Label(nova_janela, text='Data inicio:')
        label_data.grid(row=1, column=0, padx=10, pady=10)

        self.data_var = tk.StringVar()
        entry_data = ttk.Entry(nova_janela,textvariable=self.data_var)
        entry_data.grid(row=1, column=1, padx=10, pady=10)

        #Data fim
        label_data_fim = ttk.Label(nova_janela, text='Data fim:')
        label_data_fim.grid(row=2, column=0, padx=10, pady=10)

        self.data_fim_var = tk.StringVar()
        entry_data_fim = ttk.Entry(nova_janela,textvariable=self.data_fim_var)
        entry_data_fim.grid(row=2, column=1, padx=10, pady=10)

        #Hora inicio
        label_hora_inicio = ttk.Label(nova_janela, text='Hora inicio:')
        label_hora_inicio.grid(row=3, column=0, padx=10, pady=10)

        self.hora_inicio_var = tk.StringVar()
        entry_hora_inicio = ttk.Entry(nova_janela, textvariable=self.hora_inicio_var)
        entry_hora_inicio.grid(row=3, column=1, padx=10, pady=10)

        #Hora fim
        label_hora_fim = ttk.Label(nova_janela, text='Hora fim:')
        label_hora_fim.grid(row=4, column=0, padx=10, pady=10)

        self.hora_fim_var = tk.StringVar()
        entry_hora_fim = ttk.Entry(nova_janela, textvariable=self.hora_fim_var)
        entry_hora_fim.grid(row=4, column=1, padx=10, pady=10)

        botao_criar_reserva = ttk.Button(nova_janela, text='Criar Reserva', command= lambda quadras_var=self.quadras_var, 
                                         data_var = self.data_var, data_fim_var = self.data_fim_var, 
                                         hora_inicio_var = self.hora_inicio_var, hora_fim_var = self.hora_fim_var: 
                                         self.criar_reserva_quadra(quadras_var.get(),'123', data_var.get(), data_fim_var.get(), hora_inicio_var.get(), 
                                                                   hora_fim_var.get()))
        botao_criar_reserva.grid(row=5, column=0, columnspan=2, pady=10)

    def buscar_reserva(self, nome_quadra_var):
        dados_reserva = self.controller.visualizarReserva(nome_quadra_var)
        if dados_reserva:
            index = 0
            for i in dados_reserva:
                nova_janela = tk.Toplevel(self)
                nova_janela.title(f'{nome_quadra_var} reserva {index}')
                label_nome_quadra = ttk.Label(nova_janela, text=f'{nome_quadra_var} reserva {index}')
                label_nome_quadra.pack(pady=5,padx=30)

                label_nome_usuario = ttk.Label(nova_janela, text=f'Data inicio: {i[2]}')
                label_nome_usuario.pack(pady=5,padx=30)

                label_quadra = ttk.Label(nova_janela, text=f'Data fim: {i[3]}')
                label_quadra.pack(pady=5,padx=30)

                label_data = ttk.Label(nova_janela, text=f'Horario inicio: {i[4]}')
                label_data.pack(pady=5,padx=30)

                label_hora = ttk.Label(nova_janela, text=f'Horario fim: {i[5]}\n')
                label_hora.pack(pady=5,padx=30)
                index += 1

    def visualizar_reserva(self):
        nova_janela = tk.Toplevel(self)
        nova_janela.title('Visualizar Reserva')
        label_hora = ttk.Label(nova_janela, text=f'Nome da quadra:')
        label_hora.pack(pady=10)
        nome_quadra_var = tk.StringVar()
        entry_quadra_var = ttk.Entry(nova_janela, textvariable=nome_quadra_var)
        entry_quadra_var.pack(pady=10)
        botao_buscar_reserva = ttk.Button(nova_janela, text='Buscar', command= lambda nome = nome_quadra_var: self.buscar_reserva(nome.get()))
        botao_buscar_reserva.pack(pady=10)

    def registrar_presença(self):
        nova_janela = tk.Toplevel(self)
        nova_janela.title('Registrar Presença')


        label_nome_reserva = ttk.Label(nova_janela, text='Nome Quadra:')
        label_nome_reserva.grid(row=1, column=0, padx=10, pady=10)
        nome_quadra_var = tk.StringVar()
        entry_nome_quadra = ttk.Entry(nova_janela,textvariable=nome_quadra_var)
        entry_nome_quadra.grid(row=1, column=1, padx=10, pady=10)

        label_dia = ttk.Label(nova_janela, text='Dia:')
        label_dia.grid(row=2, column=0, padx=10, pady=10)
        dia_var = tk.StringVar()
        entry_dia = ttk.Entry(nova_janela,textvariable=dia_var)
        entry_dia.grid(row=2, column=1, padx=10, pady=10)

        botao_registrar_presenca = ttk.Button(nova_janela,text='Registar', command= lambda dia_var = dia_var, matricula = self.matricula,
                                              nova_janela = nova_janela, nome_quadra_var = nome_quadra_var: self.verifica_quadra(matricula, nome_quadra_var.get(),dia_var.get(), nova_janela))
        botao_registrar_presenca.grid(row=3, column = 0, padx=10, pady=10)
    
    def criar_reserva_quadra(self, quadraid, matricula, data_inicio,data_fim, horario_inicio, horario_fim):
        resultado = self.controller.save_reserva(quadraid, matricula, data_inicio, data_fim, horario_inicio, horario_fim)
        if resultado:
            self.show_success('Reservado!')
        else:
            self.show_error('Não Reservado')

    def verifica_quadra(self,matricula, quadra, dia, nova_janela):
        boolean = self.controller.verifica_quadra(matricula, quadra, dia)
        self.message_label = ttk.Label(nova_janela, text='', foreground='red')
        self.message_label.grid(row=2, column=2, sticky=tk.W)
        if boolean == True:
            self.show_success('Presença registrada!')
        else:
            
            self.show_error('Quadra nao encontrada')
        
    def set_controller(self, controller):
        self.controller = controller

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)
    
    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label.after(3000, self.hide_message)  

    def hide_message(self):
        self.message_label['text'] = ''


