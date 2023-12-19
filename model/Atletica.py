from model import User

class Atletica(User.User):
    def __init__(self, nome, email, telefone, data_nascimento, cidade, departamento, senha):
        super().__init__('10000', senha, nome=nome, tipo='Atletica')
        self.email = email
        self.cargo = ''
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.cidade = cidade
        self.departamento = departamento
        pass