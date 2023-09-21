

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, nome, matricula, tipo, email, cargo, telefone, data_nascimento, cidade, departamento, senha):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.criaUser(nome=nome,matricula = matricula, tipo = tipo, email = email, cargo = cargo, telefone = telefone, data_nascimento = data_nascimento,cidade = cidade, departamento = departamento, senha = senha)

            # show a success message
            self.view.show_success(f'Nome: {nome}, Matricula: {matricula}, Tipo: {tipo}')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)        