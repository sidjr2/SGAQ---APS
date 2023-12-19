import tkinter as tk
from tkinter import ttk
from persistance import Database
from controller import Strategy as st

class LoginView(ttk.Frame):
    
    def __init__(self, frame):
        super().__init__()
    
    def set_controller(self, controller):
        self.controller = controller

    def realiza_login(self, matricula, senha):
        login = self.login(matricula, senha) 
        if login !=0:
            match login[0][1]:
                case 'Adm':
                    self.hideframe(self.frame)
                    self.adm(self.frame, login[0][0])
                case 'Aluno':
                    self.hideframe(self.frame)
                    self.aluno(self.frame, login[0][0])
                case 'Atletica':
                    self.hideframe(self.frame)
                    self.atletica(self.frame, login[0][0])
                case 'Funcionario':
                    self.hideframe(self.frame)
                    self.funcionario(self.frame, login[0][0])
                case 'Professor':
                    self.hideframe(self.frame)
                    self.professor(self.frame,login[0][0])       
        else:
            pass 

    def draw_view(self):
        self.frame = ttk.Frame()
        self.frame.pack(padx=10, pady=10)
        self.label_matricula = ttk.Label(self.frame,text='Tela Login')
        self.label_matricula.pack(pady=10)

        self.label_matricula = ttk.Label(self.frame,text='Matricula')
        self.label_matricula.pack()

        self.var_matricula = tk.StringVar()
        self.entry_matricula = ttk.Entry(self.frame,textvariable = self.var_matricula)
        self.entry_matricula.pack()

        self.label_senha = ttk.Label(self.frame,text='Senha')
        self.label_senha.pack()

        self.var_senha = tk.StringVar()
        self.entry_senha = ttk.Entry(self.frame, textvariable=self.var_senha)
        self.entry_senha.pack()

        self.button_login = ttk.Button(self.frame, text='Login', command= lambda matricula = self.var_matricula, 
                                      senha = self.var_senha : self.realiza_login(matricula.get(), senha.get()))
        self.button_login.pack(pady=10)

    def login(self, matricula, senha):
        user = Database.Users()
        if matricula != '' and senha != '':
            resultado = user.search('matricula, tipo', 'usuarios', f'matricula = "{matricula}" AND senha = "{senha}"')
        else:
            resultado = []
        if len(resultado) != 0 or len(resultado) > 1:
            return resultado #Sucesso
        else:
            return 0 #Falha
    
    def adm(self, frame, matricula):
        from view import AdmView
        controller = st.Controller(st.AdmController(),matricula)
        view = AdmView.AdmView(frame)
        view.set_controller(controller)
        view.drawview()

    def aluno(self, frame, matricula):
        from view import AlunoView
        controller = st.Controller(st.Aluno(), matricula)
        view = AlunoView.AlunoView(frame)
        view.set_controller(controller)

        view.drawview()
    def professor(self, frame, matricula):
        from view import ProfessorView
        controller = st.Controller(st.Professor(), matricula)
        view = ProfessorView.ProfessorView(frame)
        view.set_controller(controller)
        view.drawview()

    def atletica(self, frame, matricula):
        from view import AtleticaView
        controller = st.Controller(st.Atletica(), matricula)
        view = AtleticaView.AtleticaView(frame)
        view.set_controller(controller)
        view.drawview()

    def funcionario(self, frame, matricula):
        from view import FuncionarioView
        controller = st.Controller(st.Funcionario(), matricula)
        view = FuncionarioView.FuncionarioView(frame)
        view.set_controller(controller)
        view.drawview()

    def hideframe(self, frame):
        frame.destroy()
      
        