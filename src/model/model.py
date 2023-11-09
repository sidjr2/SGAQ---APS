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
    def __init__(self, quadraid, local, nome, horario_limpeza, capacidade, horario_disponivel):
        self.quadraid = quadraid
        self.nome = nome
        self.local = local
        self.capacidade = capacidade
        self.horario_disponivel = horario_disponivel
        self.horario_limpeza = horario_limpeza


class Model:
    def __init__(self):
        self.users = []
        self.quadras = []
        self.userid = 0
        self.quadraid = 0
    def criaUser(self, nome, matricula, tipo, email, cargo, telefone , data_nascimento, cidade, departamento, senha):
        user = User(userid = self.userid, nome = nome, matricula = matricula, tipo = tipo, email=email,cargo=cargo,telefone=telefone,data_nascimento=data_nascimento, cidade = cidade, departamento = departamento, senha = senha)
        self.users.append(user)
    
        with open('users.txt', 'a') as f:
            f.write(f'{str(self.userid)}, {user.nome}, {user.matricula}, {user.tipo}, {user.email}, {user.cargo}, {user.telefone}, {user.data_nascimento}\n')

        self.userid += 1

    def criaQuadra(self, local, nome, horario_limp, horario_disp, capacidade):
        quadra = Quadra(quadraid = self.quadraid, local = local, horario_limpeza = horario_limp, horario_disponivel = horario_disp, nome = nome,capacidade=capacidade)
        self.quadras.append(quadra)
        with open('quadra.txt', 'a') as f:
            f.write(f'{str(self.quadraid)}, {nome}, {local}, {capacidade}, {horario_disp}, {horario_limp}')

        self.quadraid += 1