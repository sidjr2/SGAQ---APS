import re
from typing import Any

class User:
    def __init__(self, userid, nome, tipo, matricula):
        self.userid = userid 
        self.nome = nome
        self.tipo = tipo
        self.matricula = matricula

    def __str__(self):
        print(self.userid + self.nome + self.tipo + self.matricula)
        

class Quadra: 
    def __init__(self, quadraid, local):
        self.quadraid = quadraid
        self.local = local


class Model:
    def __init__(self):
        self.users = []
        self.quadras = []
        self.userid = 0

    def criaUser(self, nome, matricula, tipo):
        user = User(userid = self.userid, nome = nome, matricula = matricula, tipo = tipo)
        self.users.append(user)
    
        with open('users.txt', 'a') as f:
            f.write(f'{str(self.userid)}, {user.nome}, {user.matricula}, {user.tipo}\n')

        self.userid += 1

    def criaQuadra(self, quadra):
        self.quadras.append(quadra)