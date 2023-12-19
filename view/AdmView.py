import tkinter as tk
from tkinter import ttk
from controller import Strategy
from model.Adm import Adm
from model.Aluno import Aluno
from model.Quadra import Quadra
from model.Reserva import Reserva
from model.Atletica import Atletica
from model.Professor import Professor
from model.Funcionario import Funcionario
from view.LoginView import LoginView 


class AdmView(ttk.Frame):
    def __init__(self, frame):
        self.frame = frame

    def set_controller(self, controller):
        self.controller = controller

    def drawview(self):
        self.frame = ttk.Frame()
        self.frame.pack(padx=10, pady=10)
        label = ttk.Label(self.frame, text= 'Menu ADM')
        label.pack()

        self.user_button = ttk.Button(self.frame,text='Usuários', command = lambda frame = self.frame: self.drawusuarios(frame))
        self.user_button.pack(pady = 10)

        self.quadra_button = ttk.Button(self.frame, text= 'Quadras', command = lambda frame = self.frame: self.drawquadra(frame))
        self.quadra_button.pack(pady = 10)
        
        self.reserva_button = ttk.Button(self.frame, text= 'Reservas', command = lambda frame = self.frame: self.drawreserva(frame))
        self.reserva_button.pack(pady = 10)

        quitbutton = ttk.Button(self.frame, text= 'Deslogar', command = lambda frame = self.frame: self.quit(frame))
        quitbutton.pack(pady=10)

    def quit(self, frame):
        frame.destroy()
        view = LoginView(frame)
        view.draw_view()


    def drawusuarios(self, frame:ttk.Frame):
        frame = tk.Toplevel(frame)
        frame.title('Usuario')
        self.controller.strategy = Strategy.AdmController()
        novouser = ttk.Button(frame, text='Adicionar Usuario', command = lambda frame = frame: self.drawadduser(frame))
        novouser.pack(pady = 10)

        deleteuser = ttk.Button(frame, text= 'Deletar Usuario', command = lambda frame = frame: self.drawdeleteuser(frame))
        deleteuser.pack(pady = 10)

        veruser = ttk.Button(frame, text= 'Visualizar Usuarios', command = lambda frame = frame: self.drawviewuser(frame))
        veruser.pack(pady = 10)


    def drawquadra(self, frame):
        frame = tk.Toplevel(frame)
        frame.title('Quadra')
        self.controller.strategy = Strategy.QuadraController()
        novaquadra = ttk.Button(frame, text='Adicionar Quadra', command= lambda frame = frame: self.drawaddquadra(frame))
        novaquadra.pack(pady = 10)

        deletequadra = ttk.Button(frame, text= 'Deletar Quadra', command= lambda frame = frame: self.drawdeletequadra(frame))
        deletequadra.pack(pady = 10)

        verquadra = ttk.Button(frame, text= 'Visualizar Quadras', command= lambda frame = frame: self.drawviewquadra(frame))
        verquadra.pack(pady = 10)

    def drawreserva(self, frame):
        frameadd = tk.Toplevel(frame)
        self.controller.strategy = Strategy.ReservaController()
        novareserva = ttk.Button(frameadd, text='Adicionar Reserva', command= lambda frame = frame: self.drawaddreserva(frame))
        novareserva.pack(pady = 10)

        deletereserva = ttk.Button(frameadd, text= 'Deletar Reserva', command= lambda frame = frame: self.drawdeletereserva(frame))
        deletereserva.pack(pady = 10)

        verreserva = ttk.Button(frameadd, text= 'Visualizar Reserva', command= lambda frame = frame: self.drawviewreserva(frame))
        verreserva.pack(pady = 10)
    
    def drawaddquadra(self, frame):
        frameadd = tk.Toplevel(frame)
        frameadd.title('Adicionar Usuario')
        titulo = ttk.Label(frameadd, text='Adicionar Quadra', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10)
        entries = []
        labels = ['Nome', 'Local', 'Capacidade', 'Horário Disponível', 'Horário Limpeza']

        for i in labels:
            label = ttk.Label(frameadd, text=i)
            label.pack()

            entry = ttk.Entry(frameadd)
            entry.pack()
            entries.append(entry)
        button = ttk.Button(frameadd, text= 'Adicionar Quadra', command= lambda entries = entries: self.inserequadra(entries))
        button.pack(pady=10)

    def drawaddreserva(self, frame):
        frameadd = tk.Toplevel(frame)
        frameadd.title('Adicionar Reserva')
        titulo = ttk.Label(frameadd, text='Adicionar Reserva', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10)
        entries = []
        labels = ['Data inicio','Data fim', 'Horario inicio', 'Horario fim']
        entries.append(self.controller.matricula)
        label = ttk.Label(frameadd, text='Quadras')
        label.pack()
        self.controller.strategy = Strategy.QuadraController()
        combobox = ttk.Combobox(frameadd, values=self.controller.get_quadras())
        combobox.pack()
        self.controller.strategy = Strategy.ReservaController()
        entries.append(combobox)
        for i in labels:
            label = ttk.Label(frameadd, text=i)
            label.pack()

            entry = ttk.Entry(frameadd)
            entry.pack()
            entries.append(entry)
        button = ttk.Button(frameadd, text= 'Adicionar Reserva', command= lambda entries = entries: self.inserereserva(entries))
        button.pack(pady=10)

    def drawdeletereserva(self, frame):
        frameadd = tk.Toplevel(frame)
        frameadd.title('Deletar Reserv')
        titulo = ttk.Label(frameadd, text='Deletar Reserva', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10)

        label = ttk.Label(frameadd,text='Selecione a reserva:')
        label.pack(pady=10)
        self.controller.strategy = Strategy.ReservaController()
        reserva = self.controller.get_quadras()
        combobox = ttk.Combobox(frameadd, values = reserva)
        combobox['state'] = 'readonly'
        combobox.pack()

        delete_button = ttk.Button(frameadd,text='Deletar', command= lambda text = combobox: self.deletereserva(text.get()))
        delete_button.pack(pady=10)

    def drawdeletequadra(self, frame):
        frameadd = tk.Toplevel(frame)
        frameadd.title('Deletar Quadra')
        titulo = ttk.Label(frameadd, text='Deletar Quadra', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10)

        label = ttk.Label(frameadd,text='Selecione a quadra:')
        label.pack(pady=10)
        quadras = self.controller.get_quadras()
        combobox = ttk.Combobox(frameadd, values = quadras)
        combobox['state'] = 'readonly'
        combobox.pack()

        delete_button = ttk.Button(frameadd,text='Deletar', command= lambda text = combobox: self.deletequadra(text.get()))
        delete_button.pack(pady=10)

    def drawadduser(self, frame):
        frameadd = tk.Toplevel(frame)
        frameadd.title('Adicionar Usuario')
        titulo = ttk.Label(frameadd, text='Adicionar Usuário', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10)

        label = ttk.Label(frameadd,text='Selecione o tipo:')
        label.pack(pady=10)

        combobox_var = tk.StringVar()
        combobox = ttk.Combobox(frameadd,textvariable=combobox_var)
        combobox['values'] = ('Adm', 'Aluno', 'Atletica', 'Funcionario', 'Professor')
        combobox['state'] = 'readonly'
        combobox.pack()

        button = ttk.Button(frameadd, text= 'Escolher', command = lambda var = combobox, frame = frame, frameadd = frameadd: self.selecttipo(var.get(), frame, frameadd))
        button.pack()

        
    def drawdeleteuser(self, frame):
        frameadd = tk.Toplevel(frame)
        frameadd.title('Deletar Usuario')
        titulo = ttk.Label(frameadd, text='Deletar Usuário', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10)

        label = ttk.Label(frameadd,text='Selecione o usuário (por matricula):')
        label.pack(pady=10)
        users = self.controller.get_users()
        combobox = ttk.Combobox(frameadd, values = users)
        combobox['state'] = 'readonly'
        combobox.pack()

        delete_button = ttk.Button(frameadd,text='Deletar', command= lambda text = combobox: self.deleteuser(text.get()))
        delete_button.pack(pady=10)

    def drawviewquadra(self, frame):
        self.controller.strategy = Strategy.QuadraController()
        quadras = self.controller.get_quadras()
        frameadd = tk.Toplevel(frame)
        frameadd.title('Visualizar Quadras')
        titulo = ttk.Label(frameadd, text='Visualizar Quadras', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10, side='top')
        for i in quadras:
            label = ttk.Label(frameadd, text='Nome: ')
            label.pack()
            label = ttk.Label(frameadd, text=f'{i[0]}')
            label.pack()
            label = ttk.Label(frameadd, text=f'----')
            label.pack()
    

    def drawviewuser(self, frame):
        users = self.controller.get_users()
        frameadd = tk.Toplevel(frame)
        frameadd.title('Visualizar Usuario')
        titulo = ttk.Label(frameadd, text='Visualizar Usuários', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10, side='top')
        for i in users:
            label = ttk.Label(frameadd, text='Nome: ')
            label.pack()
            label = ttk.Label(frameadd, text=f'{i[0]}')
            label.pack()

            label = ttk.Label(frameadd, text='Matricula:')
            label.pack()

            label = ttk.Label(frameadd, text=f'{i[1]}')
            label.pack()

            label = ttk.Label(frameadd, text=f'----')
            label.pack()

    def drawviewreserva(self, frame):
        self.controller.strategy = Strategy.ReservaController()
        reserva = self.controller.get_quadras()
        frameadd = tk.Toplevel(frame)
        frameadd.title('Visualizar Reservas')
        titulo = ttk.Label(frameadd, text='Visualizar Reservas', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10, side='top')
        for i in reserva:
            label = ttk.Label(frameadd, text='Quadra: ')
            label.pack()
            label = ttk.Label(frameadd, text=f'{i[0]}')
            label.pack()

            label = ttk.Label(frameadd, text='Matricula:')
            label.pack()

            label = ttk.Label(frameadd, text=f'{i[1]}')
            label.pack()

            label = ttk.Label(frameadd, text='Data inicio:')
            label.pack()

            label = ttk.Label(frameadd, text=f'{i[2]}')
            label.pack()

            label = ttk.Label(frameadd, text='Horario inicio:')
            label.pack()

            label = ttk.Label(frameadd, text=f'{i[3]}')
            label.pack()

            label = ttk.Label(frameadd, text=f'----')
            label.pack()
            
    

    def selecttipo(self, var, frame, frameadd):
        frameadd.destroy()
        frameadd = tk.Toplevel(frame)
        match var:
            case 'Adm':
                entries = [] 
                labels = ['Nome', 'Matricula', 'Email', 'Cargo', 'Telefone', 'Data_nascimento', 'Cidade', 'Departamento', 'Senha']
                l = ttk.Label(frameadd, text='Adm')
                l.pack()
                for i in labels:
                    label = ttk.Label(frameadd, text=i)
                    label.pack(padx=10)
                
                    entry = ttk.Entry(frameadd)
                    entry.pack(padx=10)
                    
                  
                    entries.append(entry)
                botao_salvar = ttk.Button(frameadd, text= 'Salvar', command= lambda entries = entries: self.insereadm(entries))
                botao_salvar.pack(padx=10,pady=10)

            case 'Funcionario':
                entries = [] 
                labels = ['Nome', 'Matricula', 'Email', 'Cargo', 'Telefone', 'Data_nascimento', 'Cidade', 'Departamento', 'Senha']
                l = ttk.Label(frameadd, text='Funcionario')
                l.pack()
                for i in labels:
                    label = ttk.Label(frameadd, text=i)
                    label.pack(padx=10)
                
                    entry = ttk.Entry(frameadd)
                    entry.pack(padx=10)
                    
                  
                    entries.append(entry)
                botao_salvar = ttk.Button(frameadd, text= 'Salvar', command= lambda entries = entries: self.inserefuncionario(entries))
                botao_salvar.pack(padx=10,pady=10)
            case 'Aluno':
                entries = [] 
                labels = ['Nome', 'Matricula', 'Email', 'Telefone', 'Data_nascimento', 'Cidade', 'Departamento', 'Senha']
                l = ttk.Label(frameadd, text='Aluno')
                l.pack()
                for i in labels:
                    label = ttk.Label(frameadd, text=i)
                    label.pack(padx=10)
                
                    entry = ttk.Entry(frameadd)
                    entry.pack(padx=10)
                    
                  
                    entries.append(entry)
                botao_salvar = ttk.Button(frameadd, text= 'Salvar', command= lambda entries = entries: self.inserealuno(entries))
                botao_salvar.pack(padx=10,pady=10)
            
            case 'Atletica':
                entries = [] 
                labels = ['Nome','Email', 'Telefone', 'Data_nascimento', 'Cidade', 'Departamento', 'Senha']
                l = ttk.Label(frameadd, text='Atletica')
                l.pack()
                for i in labels:
                    label = ttk.Label(frameadd, text=i)
                    label.pack(padx=10)
                
                    entry = ttk.Entry(frameadd)
                    entry.pack(padx=10)
                    
                  
                    entries.append(entry)
                botao_salvar = ttk.Button(frameadd, text= 'Salvar', command= lambda entries = entries: self.insereatletica(entries))
                botao_salvar.pack(padx=10,pady=10)
            
            case 'Professor':
                entries = [] 
                labels = ['Nome', 'Matricula', 'Email', 'Cargo', 'Telefone', 'Data_nascimento', 'Cidade', 'Departamento', 'Senha']
                l = ttk.Label(frameadd, text='Professor')
                l.pack()
                for i in labels:
                    label = ttk.Label(frameadd, text=i)
                    label.pack(padx=10)
                
                    entry = ttk.Entry(frameadd)
                    entry.pack(padx=10)
                    
                  
                    entries.append(entry)
                botao_salvar = ttk.Button(frameadd, text= 'Salvar', command= lambda entries = entries: self.insereprofessor(entries))
                botao_salvar.pack(padx=10,pady=10)

    def insereadm(self, entries):
        self.controller.strategy = Strategy.AdmController()
        adm = Adm(nome=entries[0].get(),matricula=entries[1].get()
                  ,email=entries[2].get(),cargo=entries[3].get(),telefone=entries[4].get(),data_nascimento=entries[5].get(),
                  cidade=entries[6].get(),departamento=entries[7].get(),senha=entries[8].get())
        self.controller.inserir(adm)
    
    def inserefuncionario(self,entries):
        self.controller.strategy = Strategy.AdmController()
        funcionario = Funcionario(nome=entries[0].get(),matricula=entries[1].get()
                  ,email=entries[2].get(),cargo=entries[3].get(),telefone=entries[4].get(),data_nascimento=entries[5].get(),
                  cidade=entries[6].get(),departamento=entries[7].get(),senha=entries[8].get())
        self.controller.inserir(funcionario)

    def inserealuno(self, entries):
        self.controller.strategy = Strategy.AdmController()
        aluno = Aluno(nome=entries[0].get(),matricula=entries[1].get()
                  ,email=entries[2].get(),telefone=entries[3].get(),data_nascimento=entries[4].get(),
                  cidade=entries[5].get(),departamento=entries[6].get(),senha=entries[7].get())
        self.controller.inserir(aluno)

    def insereatletica(self, entries):
        self.controller.strategy = Strategy.AdmController()
        atletica = Atletica(nome=entries[0].get(),email=entries[1].get(),telefone=entries[2].get(),data_nascimento=entries[3].get(),
                  cidade=entries[4].get(),departamento=entries[5].get(),senha=entries[6].get())
        self.controller.inserir(atletica)

    def insereprofessor(self, entries):
        self.controller.strategy = Strategy.AdmController()
        professor = Professor(nome=entries[0].get(),matricula=entries[1].get()
                  ,email=entries[2].get(),cargo=entries[3].get(),telefone=entries[4].get(),data_nascimento=entries[5].get(),
                  cidade=entries[6].get(),departamento=entries[7].get(),senha=entries[8].get())
        self.controller.inserir(professor)

    def inserequadra(self, entries):
        self.controller.strategy = Strategy.QuadraController()
        quadra = Quadra(nome=entries[0].get(), local=entries[1].get(), capacidade=entries[2].get(),horario_disponivel=entries[3].get(), horario_limpeza=entries[4].get())
        self.controller.inserir(quadra)

    def inserereserva(self, entries):
        self.controller.strategy = Strategy.ReservaController()
        reserva = Reserva(nomequadra=entries[1].get(),matricula=entries[0],data_inicio=entries[2].get(),data_fim=entries[3].get(),horario_inicio=entries[4].get(),horario_fim=entries[5].get())
        self.controller.inserir(reserva)

    def deletequadra(self, nome):
        self.controller.strategy = Strategy.QuadraController()
        self.controller.deletar(nome)

    def deleteuser(self, text):
        self.controller.strategy = Strategy.AdmController()
        lista = text.split()
        self.controller.delete_user(lista[1])

    def deletereserva(self,text):
        self.controller.strategy = Strategy.ReservaController()
        texto = text.split()
        self.controller.deletar(texto)



                
                
    
    