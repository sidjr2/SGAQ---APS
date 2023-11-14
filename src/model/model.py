import re
from typing import Any
import mysql.connector.cursor

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DarknessKD1.",
    database="pytest"
)
mycursor = mydb.cursor()


class User:
    def __init__(self):
        mycursor.execute('SELECT userid, nome, tipo, matricula, email, cargo, telefone, data_nascimento, cidade, departamento, senha, punicao FROM usuarios')
        resultados = mycursor.fetchall()
        for i in resultados:
            self.userid = i[0]
            self.nome = i[1]
            self.tipo = i[2]
            self.matricula = i[3]
            self.email = i[4]
            self.cargo = i[5]
            self.telefone = i[6]
            self.data_nascimento = i[7]
            self.cidade = i[8]
            self.departamento = i[9]
            self.senha = i[10]
            self.punicao = i[11]


class Quadra:
    def __init__(self):
        self.quadraid = []
        self.local = []
        self.nome = []
        self.capacidade = []
        self.horario_disponivel = []
        self.horario_limpeza = []
        mycursor.execute('SELECT quadraid ,nome, local, capacidade, horario_disponivel, horario_limpeza FROM quadras')
        resultados = mycursor.fetchall()
        for i in resultados:
            self.quadraid.append(i[0])
            self.nome.append(i[1])
            self.local.append(i[2])
            self.capacidade.append(i[3])
            self.horario_disponivel.append(i[4])
            self.horario_limpeza.append(i[5])
        


class Model:
    def __init__(self):
        self.colunasusuario = ['nome', 'matricula', 'tipo', 'email', 'telefone', 'data_nascimento', 'cidade', 'senha',
                               'cargo', 'departamento']
        self.colunasquadra = ['nome', 'local', 'capacidade', 'horario_disponivel', 'horario_limpeza']
        self.cursor = mycursor
        self.db = mydb
    def criaUser(self, nome, matricula, tipo, email, cargo, telefone, data_nascimento, cidade, departamento, senha):
        sql = "INSERT INTO usuarios (nome, tipo, matricula, email, cargo, telefone, data_nascimento, cidade, " \
              "departamento, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        val = (
        f"{nome}", f"{tipo}", f"{matricula}", f"{email}", f"{cargo}", f"{telefone}", f"{data_nascimento}", f"{cidade}",
        f"{departamento}", f"{senha}")
        mycursor.execute(sql, val)
        mydb.commit()

    def criaQuadra(self, local, nome, horario_limp, horario_disp, capacidade):
        sql = "INSERT INTO quadras (nome, local, capacidade, horario_disponivel, horario_limpeza) VALUES (%s, %s, %s, %s, %s)"
        val = (f"{nome}", f"{local}", f"{capacidade}", f"{horario_disp}", f"{horario_limp}")
        mycursor.execute(sql, val)
        mydb.commit()

    def RealizaLogin(self, matricula, senha):
        mycursor.execute('SELECT matricula, senha, tipo FROM usuarios')
        i = mycursor.fetchall()
        for x in i:
            if x[0] == matricula and x[1] == senha:
                return True, x[2]
        return False, None

    def retornaUser(self):
        mycursor.execute('SELECT nome, matricula FROM usuarios')
        i = mycursor.fetchall()
        return i

    def retornaQuadra(self):
        mycursor.execute('SELECT quadraid ,nome, local FROM quadras')
        i = mycursor.fetchall()
        return i

    def deleteUser(self, matricula):
        mycursor.execute(f"DELETE FROM usuarios WHERE matricula = '{matricula}'")
        mydb.commit()

    def deleteQuadra(self, quadraid):
        mycursor.execute(f"DELETE FROM quadras WHERE quadraid = {quadraid}")
        mydb.commit()

    def editUser(self, matricula, alteracoes):
        print(matricula, alteracoes)
        index = 0
        for i in alteracoes:
            mycursor.execute(
                f"UPDATE usuarios SET {self.colunasusuario[index]} = '{i}' WHERE matricula = '{matricula}'")
            if index == 1:
                matricula = i
            index += 1
        mydb.commit()

    def editQuadra(self, quadraid, alteracoes):
        print(quadraid, alteracoes)
        index = 0
        for i in alteracoes:
            mycursor.execute(f"UPDATE quadras SET {self.colunasquadra[index]} = '{i}' WHERE quadraid = '{quadraid}'")
            index += 1
        mydb.commit()
