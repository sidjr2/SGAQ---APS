import re
from typing import Any

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
    def __init__(self, quadraid, local):
        self.quadraid = quadraid
        self.local = local


class Model:
    def __init__(self):
        self.users = []
        self.quadras = []
        self.userid = 0

    def criaUser(self, nome, matricula, tipo, email, cargo, telefone , data_nascimento, cidade, departamento, senha):
        user = User(userid = self.userid, nome = nome, matricula = matricula, tipo = tipo, email=email,cargo=cargo,telefone=telefone,data_nascimento=data_nascimento, cidade = cidade, departamento = departamento, senha = senha)
        self.users.append(user)
    
        with open('users.txt', 'a') as f:
            f.write(f'{str(self.userid)}, {user.nome}, {user.matricula}, {user.tipo}, {user.email}, {user.cargo}, {user.telefone}, {user.data_nascimento}\n')

        self.userid += 1

    def criaQuadra(self, quadra):
        self.quadras.append(quadra)