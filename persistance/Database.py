import mysql.connector
from abc import ABC, abstractmethod
#Conexão bd
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DarknessKD1.",
    database="pytest"
)

class DAO(ABC):
    _instance = None
    @abstractmethod
    def __init__(self):
        self.db = mydb
        self.cursor = mydb.cursor()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @abstractmethod
    def insert(self, sql, values):
        pass

    @abstractmethod
    def search(self, coluna, tabela, parametro):
        sql = f"SELECT {coluna} FROM {tabela} WHERE {parametro}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    @abstractmethod
    def delete_user(self, coluna, tabela, parametro):
        pass

    @abstractmethod
    def get(self):
        pass

class Users(DAO):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, sql, values):
        return super().insert(sql, values)  
    
    def search(self, coluna, tabela, parametro):
        resultado = super().search(coluna, tabela, parametro)
        return resultado
    
    def delete_user(self, coluna, tabela, parametro):
        return super().delete(coluna, tabela, parametro)
    
    def get(self):
        return super().get()

    

class Adm(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, sql, values):
        self.cursor.execute(sql,values)
        self.db.commit()

    def delete_user(self, matricula):
        sql = f"DELETE FROM usuarios WHERE matricula = '{matricula}'"
        self.cursor.execute(sql)
        self.db.commit()

    def search(self, coluna, tabela, parametro):
        return super().search(coluna, tabela, parametro)
    
    def get(self, colunas, tabela):
        sql = f'SELECT {colunas} FROM {tabela}'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    
class Aluno(DAO):
    def __init__(self):
        self.db = mydb
        self.cursor = mydb.cursor()
    
    def foo(self):
        return super().foo()

    def insert(self, nome_tabela, nome_valores):
        return super().insert(nome_tabela, nome_valores)
    
class Atletica(DAO):
    def __init__(self):
        self.db = mydb
        self.cursor = mydb.cursor()

class Funcionario(DAO):
    def __init__(self):
        self.db = mydb
        self.cursor = mydb.cursor()

class Professor(DAO):
    def __init__(self):
        self.db = mydb
        self.cursor = mydb.cursor()

class Quadra(DAO):
    def __init__(self):
        self.db = mydb
        self.cursor = mydb.cursor()

    def search(self, coluna, tabela, parametro):
        return super().search(coluna, tabela, parametro)
    
    def get(self):
        sql = "SELECT nome FROM quadras"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def insert(self, sql, values):
        self.cursor.execute(sql, values)
        self.db.commit()
    
    def delete_user(self, nome):
        sql = f"DELETE FROM quadras WHERE nome = '{nome}'"
        self.cursor.execute(sql)
        self.db.commit()

class Reserva(DAO):

    def __init__(self):
        self.db = mydb
        self.cursor = mydb.cursor()

    def search(self, coluna, tabela, parametro):
        return super().search(coluna, tabela, parametro)
    
    def get(self):
        sql = "SELECT quadraid, matricula, data_inicio, horario_inicio FROM reservas"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def insert(self, sql, values):
        self.cursor.execute(sql, values)
        self.db.commit()
    
    def delete_user(self, nome, matricula, dia, horario_inicio):
        sql = f"DELETE FROM reservas WHERE quadraid = '{nome}' AND horario_inicio = '{horario_inicio}' AND matricula = '{matricula}' AND data_inicio ='{dia}'"
        self.cursor.execute(sql)
        self.db.commit()

class Presenca(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, sql, values):
        self.cursor.execute(sql,values)
        self.db.commit()

    def delete_user(self, matricula):
        pass

    def search(self, coluna, tabela, parametro):
        return super().search(coluna, tabela, parametro)
    
    def get(self, colunas, tabela):
        sql = f'SELECT {colunas} FROM {tabela}'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
       

