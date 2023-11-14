
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

    
class ControllerGeral:
    def __init__(self, quadras, model, view):
          self.model = model
          self.view = view
          self.quadras = quadras
    def fetch_quadras(self):
        quadras = self.quadras.nome
        return quadras
    
    def save_reserva(self, quadraid, matricula, data_inicio,data_fim, horario_inicio, horario_fim):
        try:
            self.model.cursor.execute(f"SELECT quadraid FROM quadras WHERE nome = '{quadraid}'")
            true_quadraid = self.model.cursor.fetchall()
            sql = 'INSERT INTO reservas (quadraid, matricula, data_inicio,data_fim, horario_inicio, horario_fim) VALUES (%s, %s, %s, %s, %s, %s)'
            val = (f"{true_quadraid[0][0]}",f"{matricula}",f"{data_inicio}",f"{data_fim}",f"{horario_inicio}",f"{horario_fim}")       
            self.model.cursor.execute(sql, val)
            self.model.db.commit()
            return True
        except:
            return False
            
        

    def visualizarReserva(self, quadra):
        self.model.cursor.execute(f'SELECT quadraid FROM quadras WHERE nome = "{quadra}"')
        quadraid = self.model.cursor.fetchall()
        if len(quadraid) == 0:
            return False
        self.model.cursor.execute(f'SELECT * FROM reservas WHERE quadraid = "{quadraid[0][0]}"')
        reservas = self.model.cursor.fetchall()
        return reservas

    def verifica_quadra(self,matricula, quadra, dia):
        
        for i in self.quadras.nome:
             if i == quadra:
                self.model.cursor.execute(f"SELECT quadraid FROM quadras WHERE nome = '{quadra}'")
                quadraid = self.model.cursor.fetchall()
                self.model.cursor.execute(f"SELECT reservaid FROM reservas WHERE quadraid = '{quadraid[0][0]}'")
                reservaid = self.model.cursor.fetchall()
                sql = ('INSERT INTO  presenca (matricula, reservaid, dia) VALUES (%s, %s, %s)')
                val = (f"{matricula}",f"{reservaid[0][0]}",f"{dia}")
                self.model.cursor.execute(sql,val)
                self.model.db.commit()
                return True
        return False 
