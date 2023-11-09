
class ControllerUser:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def saveuser(self, nome, matricula, tipo, email, cargo, telefone, data_nascimento, cidade, departamento, senha):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.criaUser(nome=nome ,matricula = matricula, tipo = tipo, email = email, cargo = cargo, telefone = telefone, data_nascimento = data_nascimento ,cidade = cidade, departamento = departamento, senha = senha)

            # show a success message
            self.view.show_success(f'Nome: {nome}, Matricula: {matricula}')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

class ControllerQuadra:
            def __init__(self, model, view):
                 self.model = model
                 self.view = view

            def savequadra(self, local, nome, horario_limp, horario_disp, capacidade):
                self.model.criaQuadra(local=local ,nome=nome ,horario_limp=horario_limp ,horario_disp=horario_disp, capacidade = capacidade)
                self.view.show_success \
            (f'Nome: {nome}, Local:{local}, Capacidade: {capacidade}, Horario Disponivel: {horario_disp}, Horario Limpeza: {horario_limp}')

class ControllerMenu:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def login(self, matricula, senha):
         resultado, tipo = self.model.RealizaLogin(matricula=matricula, senha=senha)
         if resultado:
              self.view.show_success('Login feito com sucesso!')
              self.view.show_login(tipo)
         else:
              self.view.show_error('Os dados de matrícula ou senha fornecidos são inválidos.')

class ControllerAdm:
    def __init__(self, model, view):
          self.model = model
          self.view = view
    
    def savequadra(self, local, nome, horario_limp, horario_disp, capacidade):
                
                self.model.criaQuadra(local=local ,nome=nome ,horario_limp=horario_limp ,horario_disp=horario_disp, capacidade = capacidade)
                
                self.view.show_success \
            (f'Nome: {nome}, Local:{local}, Capacidade: {capacidade}, Horario Disponivel: {horario_disp}, Horario Limpeza: {horario_limp}')

    def saveuser(self, nome, matricula, tipo, email, cargo, telefone, data_nascimento, cidade, departamento, senha):
        try:

            # save the model
            self.model.criaUser(nome=nome ,matricula = matricula, tipo = tipo, email = email, cargo = cargo, telefone = telefone, data_nascimento = data_nascimento ,cidade = cidade, departamento = departamento, senha = senha)

            # show a success message
            self.view.show_success(f'Nome: {nome}, Matricula: {matricula}')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)
    
    def retornauser(self):
        retorno = self.model.retornaUser()
        return retorno
    
    def retornaquadra(self):
         retorno = self.model.retornaQuadra()
         return retorno
    
    def deleteuser(self, matricula):
         self.model.deleteUser(matricula)
    
    def deletequadra(self, matricula):
         self.model.deleteQuadra(matricula)

    def edituser(self ,matricula, alteracoes):
         matriz = []
         for i in alteracoes:
            matriz.append(i.get())
         self.model.editUser(matricula ,matriz)

    def editquadra(self, quadra, alteracoes):
        matriz = []
        for i in alteracoes:
            matriz.append(i.get())
        self.model.editQuadra(quadra, matriz)

class ControllerReserva:
    def __init__(self, model, view):
          self.model = model
          self.view = view

    def savereserva(self, reservaId, quadraid, usuarioId, data, hora):
                
        self.model.criaReserva(reservaId=reservaId,quadraid=quadraid,usuarioId=usuarioId,data=data, hora = hora)
                
        self.view.show_success(f'Reserva: {reservaId}, Local:{quadraid}, Capacidade: {usuarioId},Data:{data}, Horario: {hora}')
        
    def visualizarReserva(self, reservaId):
         self.model.visualizarReserva(reservaId)