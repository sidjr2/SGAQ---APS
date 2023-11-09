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
    def __init__(self, userid, nome, tipo, matricula, email, cargo, telefone, data_nascimento, cidade, departamento, senha):
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

class Reserva: 
    def __init__(self,reservaId, quadraid, usuarioId, data, hora):
        self.reservaId = quadraid
        self.quadraid = quadraid
        self.usuarioId = nome
        self.data = data
        self.hora = hora


class Model:
       
    def criaUser(self, nome, matricula, tipo, email, cargo, telefone , data_nascimento, cidade, departamento, senha):
        sql = "INSERT INTO usuarios (nome, tipo, matricula, email, cargo, telefone, data_nascimento, cidade, departamento, senha) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (f"{nome}", f"{tipo}",f"{matricula}",f"{email}",f"{cargo}",f"{telefone}",f"{data_nascimento}",f"{cidade}",f"{departamento}",f"{senha}")
        mycursor.execute(sql, val)
        mydb.commit()

    def criaQuadra(self, local, nome, horario_limp, horario_disp, capacidade):
        sql = "INSERT INTO quadras (nome, local, capacidade, horario_disponivel, horario_limpeza) VALUES (%s, %s, %s, %s, %s)"
        val = (f"{nome}", f"{local}",f"{capacidade}",f"{horario_disp}",f"{horario_limp}")
        mycursor.execute(sql, val)
        mydb.commit()

    def RealizaLogin(self, matricula, senha):
        mycursor.execute('SELECT matricula, senha FROM usuarios')
        resultados = mycursor.fetchall()
        for x in resultados:
            if x[0] == matricula and x[1] == senha:
                return True
        return False
    
    def retornaUser(self):
        mycursor.execute('SELECT nome, matricula FROM usuarios')
        resultados = mycursor.fetchall()
        return resultados
    
    def deleteUser(self, matricula):
        mycursor.execute(f"DELETE FROM usuarios WHERE matricula = '{matricula}'")
        mydb.commit()
    
    def criaReserva(self,reservaId, quadraid, usuarioId, data, hora):
        sql = "INSERT INTO reservas (reservaid, quadraid, usuarioid, data, hora) VALUES (%s, %s,%s,%s,%s)"
        val = (f"{reservaId}", f"{quadraid}",f"{usuarioid}",f"{data}",f"{hora}")
        mycursor.execute(sql, val)
        mydb.commit()

    def listarReservas(self):
       mycursor.execute('SELECT reservas.*, usuarios.nome AS nome_usuario, quadras.nome AS nome_quadra FROM reservas INNER JOIN usuarios ON reservas.usuarioid = usuarios.matricula INNER JOIN quadras ON reservas.quadraid = quadras.quadraid')
        resultados = mycursor.fetchall()
        return resultados

    def visualizarReserva(self,reservaid):
        mycursor.execute(f"SELECT reservas.*, usuarios.nome AS nome_usuario, quadras.nome AS nome_quadra FROM reservas INNER JOIN usuarios ON reservas.usuarioid = usuarios.matricula INNER JOIN quadras ON reservas.quadraid = quadras.quadraid WHERE reservaid = '{reservaid}'")
        resultados = mycursor.fetchall()
        return resultados