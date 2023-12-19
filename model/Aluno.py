from model import User

class Aluno(User.User):
    def __init__(self, nome, matricula, email, telefone, data_nascimento, cidade, departamento, senha) -> None:
        super().__init__(matricula, senha, nome=nome, tipo='Aluno')
        self.email = email
        self.cargo = ''
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.cidade = cidade
        self.departamento = departamento
        pass