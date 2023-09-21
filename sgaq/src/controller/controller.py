

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, nome, matricula, tipo):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.criaUser(nome, matricula, tipo)

            # show a success message
            self.view.show_success(f'Nome: {nome}, Matricula: {matricula}, Tipo: {tipo}')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)        