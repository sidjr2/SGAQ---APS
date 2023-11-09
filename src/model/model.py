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
    def __init__(self, userid, nome, tipo, matricula, email, cargo, telefone, data_nascimento, cidade, departamento,
                 senha):
        self.userid = userid
        self.nome = nome
        self.tipo = tipo
        self.matricula = matricula
        self.email = email
        self.cargo = cargo
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.cidade = cidade
        self.departamento = departamento
        self.senha = senha
        self.punicao = 0


class Quadra:
    def __init__(self, quadraid, local, nome, horario_limpeza, capacidade, horario_disponivel):
        self.quadraid = quadraid
        self.nome = nome
        self.local = local
        self.capacidade = capacidade
        self.horario_disponivel = horario_disponivel
        self.horario_limpeza = horario_limpeza


class Model:
    def __init__(self):
        self.colunasusuario = ['nome', 'matricula', 'tipo', 'email', 'telefone', 'data_nascimento', 'cidade', 'senha',
                               'cargo', 'departamento']
        self.colunasquadra = ['nome', 'local', 'capacidade', 'horario_disponivel', 'horario_limpeza']

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
        resultados = mycursor.fetchall()
        for x in resultados:
            if x[0] == matricula and x[1] == senha:
                return True, x[2]
        return False, None

    def retornaUser(self):
        mycursor.execute('SELECT nome, matricula FROM usuarios')
        resultados = mycursor.fetchall()
        return resultados

    def retornaQuadra(self):
        mycursor.execute('SELECT quadraid ,nome, local FROM quadras')
        resultados = mycursor.fetchall()
        return resultados

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
