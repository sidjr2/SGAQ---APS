from tkinter import ttk
import tkinter as tk
from controller import Strategy
from model.Reserva import Reserva
from model.Presenca import Presenca
from view.LoginView import LoginView

class FuncionarioView:
    def __init__(self, frame) -> None:
        self.frame = frame
        pass
    
    def set_controller(self, controller):
        self.controller = controller

    def drawview(self):
        self.frame = ttk.Frame()
        self.frame.pack(padx=10, pady=10)
        label = ttk.Label(self.frame, text= 'Menu Usuário')
        label.pack()

        buttonreserva = ttk.Button(self.frame, text= 'Reserva', command= lambda frame = self.frame: self.drawreserva(frame))
        buttonreserva.pack(padx=10, side= 'left')
        buttonpresença = ttk.Button(self.frame, text = 'Registrar Presença', command= lambda frame = self.frame: self.drawpresenca(frame))
        buttonpresença.pack(padx=10, side='left')

        quitbutton = ttk.Button(self.frame, text= 'Deslogar', command = lambda frame = self.frame: self.quit(frame))
        quitbutton.pack(pady=10, side= 'bottom')
    
    def quit(self, frame):
        frame.destroy()
        view = LoginView(frame)
        view.draw_view()

    def drawpresenca(self, frame):
        frameadd = tk.Toplevel(frame)
        frameadd.title('Registrar Presença')
        titulo = ttk.Label(frameadd, text='Registrar Presença', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10)

        label = ttk.Label(frameadd,text='Selecione a reserva:')
        label.pack(pady=10)
        self.controller.strategy = Strategy.ReservaController()
        reserva = self.controller.get_quadras()
        combobox = ttk.Combobox(frameadd, values = reserva)
        combobox['state'] = 'readonly'
        combobox.pack()

        label = ttk.Label(frameadd,text='Dia:')
        label.pack()
        entry = ttk.Entry(frameadd)
        entry.pack()

        registra_button = ttk.Button(frameadd,text='Registrar', command= lambda text = combobox, dia = entry: self.registrapresenca(text.get(),dia.get()))
        registra_button.pack(pady=10)
    
    def registrapresenca(self, text, dia):
        self.controller.strategy = Strategy.PresencaController()
        valores = text.split()
        presenca = Presenca(matricula=self.controller.matricula, reservaid=valores[0],dia=dia)
        self.controller.inserir(presenca)

    def drawreserva(self, frame):
        frameadd = tk.Toplevel(frame)
        self.controller.strategy = Strategy.ReservaController()
        novareserva = ttk.Button(frameadd, text='Adicionar Reserva', command= lambda frame = frame: self.drawaddreserva(frame))
        novareserva.pack(pady = 10)

        deletereserva = ttk.Button(frameadd, text= 'Deletar Reserva', command= lambda frame = frame: self.drawdeletereserva(frame))
        deletereserva.pack(pady = 10)

        verreserva = ttk.Button(frameadd, text= 'Suas Reservas', command= lambda frame = frame: self.drawviewreserva(frame))
        verreserva.pack(pady = 10)

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
        frameadd.title('Deletar Reserva')
        titulo = ttk.Label(frameadd, text='Deletar Reserva', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10)

        label = ttk.Label(frameadd,text='Selecione a reserva:')
        label.pack(pady=10)
        self.controller.strategy = Strategy.ReservaController()
        reserva = self.controller.get_quadras()
        values = []
        for i in reserva:
            if i[1] == self.controller.matricula:
                values.append(i)
        combobox = ttk.Combobox(frameadd, values = values)
        combobox['state'] = 'readonly'
        combobox.pack()

        delete_button = ttk.Button(frameadd,text='Deletar', command= lambda text = combobox: self.deletereserva(text.get()))
        delete_button.pack(pady=10)
    
    def inserereserva(self, entries):
        self.controller.strategy = Strategy.ReservaController()
        reserva = Reserva(nomequadra=entries[1].get(),matricula=entries[0],data_inicio=entries[2].get(),data_fim=entries[3].get(),horario_inicio=entries[4].get(),horario_fim=entries[5].get())
        self.controller.inserir(reserva)
    
    def deletereserva(self,text):
        self.controller.strategy = Strategy.ReservaController()
        texto = text.split()
        self.controller.deletar(texto)

    def drawviewreserva(self, frame):
        self.controller.strategy = Strategy.ReservaController()
        reserva = self.controller.get_quadras()
        frameadd = tk.Toplevel(frame)
        frameadd.title('Visualizar Reservas')
        titulo = ttk.Label(frameadd, text='Visualizar Reservas', style='Heading.TLabel')
        titulo.pack(padx=10, pady=10, side='top')
        for i in reserva:
            if i[1] == self.controller.matricula:
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