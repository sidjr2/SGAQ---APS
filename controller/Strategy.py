from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from model.Adm import Adm
from model.Quadra import Quadra
from model.Reserva import Reserva
from model.Presenca import Presenca
from persistance import Database

class Controller():
  

    def __init__(self, strategy: Strategy, matricula) -> None:
        
        self.matricula = matricula
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        

        self._strategy = strategy

    def hideframe(self, frame):
        frame.destroy()

    def inserir(self, dados):
        self._strategy.inserir(dados)
    
    def get_users(self):
        return self._strategy.get_users()
    
    def delete_user(self, matricula):
        self._strategy.delete_user(matricula)

    def get_quadras(self):
        return self._strategy.get_quadras()
    
    def deletar(self, text):
        self._strategy.deletar(text)


class Strategy(ABC):
    

    @abstractmethod
    def inserir(self, data: List):
        pass

    @abstractmethod
    def deletar(self):
        pass

    @abstractmethod    
    def editar(self):
        pass

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass

    @abstractmethod
    def get_quadras(self):
        pass

    
    





class AdmController(Strategy):
    def __init__(self) -> None:
        pass
        

    def inserir(self, data: Adm) -> List:
        sql = "INSERT INTO usuarios (nome, tipo, matricula, email, cargo, telefone, data_nascimento, cidade, departamento ,senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (f'{data.nome}',f'{data.tipo}',f'{data.matricula}',f'{data.email}',f'{data.cargo}',f'{data.telefone}',f'{data.data_nascimento}',f'{data.cidade}',f'{data.departamento}',f'{data.senha}')
        adm = Database.Adm()
        adm.insert(sql, values)
        foo = Database.Adm()
        test = Database.Users()
        test2 = Database.Users()
        if test2 is test:
            print('Works')
        if adm is foo:
            print('foo')
    def deletar(self):
        return super().deletar()
    
    def editar(self):
        return super().editar()
    
    def get_users(self):
        adm = Database.Adm()
        result = adm.get('nome, matricula', 'usuarios')
        return result
    
    def delete_user(self, matricula):
        adm = Database.Adm()
        adm.delete_user(matricula)
    
    def get_quadras(self):
        return super().get_quadras()

class Aluno(Strategy):
    def inserir(self, data: List) -> List:
        return reversed(sorted(data))
    
    def deletar(self):
        return super().deletar()
    
    def editar(self):
        return super().editar()
    
    def get_users(self):
        return super().get_users()
    
    def delete_user(self):
        return super().delete_user()
    
    def get_quadras(self):
        return super().get_quadras()
    
class Funcionario(Strategy):
    def inserir(self, data: List) -> List:
        return reversed(sorted(data))
    
    def deletar(self):
        return super().deletar()
    
    def editar(self):
        return super().editar()
    
    def get_users(self):
        return super().get_users()
    
    def delete_user(self):
        return super().delete_user()
    
    def get_quadras(self):
        return super().get_quadras()
    pass

class Professor(Strategy):
    def inserir(self, data: List) -> List:
        return reversed(sorted(data))
    
    def deletar(self):
        return super().deletar()
    
    def editar(self):
        return super().editar()
    
    def get_users(self):
        return super().get_users()
    
    def delete_user(self):
        return super().delete_user()
    
    def get_quadras(self):
        return super().get_quadras()
    pass

class Atletica(Strategy):
    def inserir(self, data: List) -> List:
        return reversed(sorted(data))
    
    def deletar(self):
        return super().deletar()
    
    def editar(self):
        return super().editar()
    
    def get_users(self):
        return super().get_users()
    
    def delete_user(self):
        return super().delete_user()
    
    def get_quadras(self):
        return super().get_quadras()
    pass

class QuadraController(Strategy):
    def inserir(self, data: Quadra):
        sql = "INSERT INTO quadras (nome, local, capacidade, horario_disponivel, horario_limpeza) VALUES (%s, %s, %s, %s, %s)"
        values = (f'{data.nome}',f'{data.local}', f'{data.capacidade}', f'{data.horario_disponivel}', f'{data.horario_limpeza}')
        quadra = Database.Quadra()
        quadra.insert(sql, values)

    def deletar(self, text):
        quadra = Database.Quadra()
        quadra.delete_user(text)

    def get_quadras(self):
        quadra = Database.Quadra()
        result = quadra.get()
        return result
    
    def get_users(self):
        return super().get_users()
    
    def delete_user(self):
        return super().delete_user()
    
    def editar(self):
        return super().editar()
    
    
    pass

class ReservaController(Strategy):
    def inserir(self, data: Reserva):
        sql = "INSERT INTO reservas (quadraid, matricula, data_inicio, data_fim, horario_inicio, horario_fim) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (f'{data.nomequadra}',f'{data.matricula}',f'{data.data_inicio}',f'{data.data_fim}',f'{data.horario_inicio}',f'{data.horario_fim}')
        reserva = Database.Reserva()
        reserva.insert(sql, values)

    def deletar(self, text):
        reserva = Database.Reserva()
        reserva.delete_user(nome=text[0], matricula= text[1], dia=text[2], horario_inicio=text[3])
    
    def get_users(self):
        return super().get_users()
    
    def delete_user(self):
        return super().delete_user()
    
    def editar(self):
        return super().editar()
    
    def get_quadras(self):
        reserva = Database.Reserva()
        result = reserva.get()
        return result
    pass

class PresencaController(Strategy):
    def inserir(self, data: Presenca) -> List:
        presenca = Database.Presenca()
        sql = "INSERT INTO presenca (matricula, reservaid, dia) VALUES (%s, %s, %s)"
        values = (f'{data.matricula}',f'{data.reservaid}',f'{data.dia}')
        presenca.insert(sql, values)
    
    def deletar(self):
        return super().deletar()
    
    def editar(self):
        return super().editar()
    
    def get_users(self):
        return super().get_users()
    
    def delete_user(self):
        return super().delete_user()
    
    def get_quadras(self):
        return super().get_quadras()
    pass

