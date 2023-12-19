from model import User

class Professor(User.User):
    def __init__(self, nome, matricula, email, cargo, telefone, data_nascimento, cidade, departamento, senha):
        super().__init__(matricula, senha, nome= nome, tipo='Professor')
        self.email = email
        self.cargo = cargo
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.cidade = cidade
        self.departamento = departamento
        pass