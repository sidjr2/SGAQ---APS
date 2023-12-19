# SISTEMA DE GERENCIAMENTO DE ALOCAÇÃO DE QUADRA - SGAQ

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-diagramas">Diagramas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-funcionalidades">Funcionalidades</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-documentação">Documentação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>


## ✍️ Autores

| [![Davi Kreppel](https://avatars.githubusercontent.com/u/66695188?v=4)](https://github.com/DaviKpp) | [![Gustavo Detomi](https://avatars.githubusercontent.com/u/31541906?v=4)](https://github.com/Gudetomi) | [![Leandro Souza](https://avatars.githubusercontent.com/u/48530574?v=4)](https://github.com/Lsouz44) | [![Matheus Nascimento](https://avatars.githubusercontent.com/u/23366884?v=4)](https://github.com/matheuznsilva) | [![Sidney Júnior](https://avatars.githubusercontent.com/u/51861308?v=4)](https://github.com/sidjr2) |
|:-:|:-:|:-:|:-:|:-:|
| [Davi Kreppel](https://github.com/DaviKpp) | [Gustavo Detomi](https://github.com/gudetomi) | [Leandro Souza](https://github.com/Lsouz44) | [Matheus Nascimento](https://github.com/matheuznsilva) | [Sidney Junior](https://github.com/sidjr2) |


## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- ![Python](https://img.shields.io/badge/Python-blue)
- ![Tkinter](https://img.shields.io/badge/Tkinter-yellow)
- ![Mysql](https://img.shields.io/badge/MySQL-blue)


## 💻 Projeto

O Sistema de Gerenciamento de Alocação de Quadra (SGAQ) é uma sistema desevolvido em python com mysql buscando otimizar o processo de reserva e utilização da quadra esportiva da Universidade Federal de São João del-Rei (UFSJ). O software oferece funcionalidades de reserva de horários, gerenciamento de equipamentos, registro de presença. Ele é destinado a diferentes perfis de usuários, como professores, atléticas, funcionários e comunidade em geral. 💰

## ⚙️ Instalação

Para instalar o sistema, siga os seguintes passos:

1. Clone o repositório do GitHub:

    ```bash
    git clone https://github.com/sidjr2/SGAQ---APS
    ```
2. Entre na pasta e instale os requirements:

    ```bash
    cd .\SGAQ---APS\
    pip install -r requirements.txt
    ```
2.1. Crie o DataBase no MySql:
  ```bash
  mysql > 
  mysql > CREATE DATABASE pytest;
  mysql > CREATE TABLE presenca (matricula VARCHAR(255), reservaid VARCHAR(255), dia VARCHAR(255));
  mysql > CREATE TABLE quadras (nome VARCHAR(255) PRIMARY KEY, local VARCHAR(255), capacidade INT, horario_disponivel VARCHAR(255), horario_limpeza VARCHAR(255));
  mysql > CREATE TABLE reservas (quadraid VARCHAR(255), matricula VARCHAR(255), data_inicio VARCHAR(255), data_fim VARCHAR(255), horario_inicio VARCHAR(255), horario_fim VARCHAR(255));
  mysql > CREATE TABLE usuarios (nome VARCHAR(255), tipo VARCHAR(255), matricula VARCHAR(255) PRIMARY KEY, email VARCHAR(255), cargo VARCHAR(255), telefone VARCHAR(255), data_nascimento VARCHAR(255), cidade VARCHAR(255), departamento VARCHAR(255), senha telefone VARCHAR(255), punicao INT)
  mysql > INSERT INTO usuarios (nome, tipo, matricula, email, cargo, telefone, data_nascimento, cidade, departamento, senha, punicao,userid) VALUES ('Nome', 'Adm', '123', 'email', 'cargo', telefone','data','cidade','depto','123','0','0')
  ```
3. Alterar as linhas do arquivo "Database.py", para puxar o seu banco de dados:
   ```bash
   cd persistance/Database.py
   mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="(alterar senha)",
        database="pytest"
    )
   ```
4. Execulte o Programa
   ```bash
     python3 main.py
   ```
6. Login de acesso
   ```bash
   Matricula: 123
   Senha: 123
   ```
## 📊 Diagramas

### Diagrama de Casos de Uso

![Diagrama de Casos de Uso](https://github.com/sidjr2/SGAQ---APS/blob/master/Diagramas/1%20-%20Diagrama%20de%20casos%20de%20uso.jpg)

##

### Diagrama de Classes

![Diagrama de Classes](https://github.com/sidjr2/SGAQ---APS/blob/master/Diagramas/2%20-%20Diagrama%20de%20classes.jpg)

##

### Diagrama de Sequência

![Diagrama de Sequência](https://github.com/sidjr2/SGAQ---APS/blob/master/Diagramas/3%20-%20Diagrama%20de%20sequência.jpg)

### Diagrama do Atividade

![Diagrama de Atividade](https://github.com/sidjr2/SGAQ---APS/blob/master/Diagramas/4%20-%20Diagrama%20de%20atividade.jpg)

### Diagrama do Máquina de Estados

![Diagrama de Máquina de Estados](https://github.com/sidjr2/SGAQ---APS/blob/master/Diagramas/5%20-%20Diagrama%20de%20máquina%20de%20estados.jpg)

### Diagrama do Pacotes

![Diagrama de Pacotes](https://github.com/sidjr2/SGAQ---APS/blob/master/Diagramas/6%20-%20Diagrama%20de%20implantação.jpg)


## 📄 Documentação

Consulte o arquivo PDF [APS-SGAQ](https://github.com/sidjr2/SGAQ---APS/blob/master/Diagramas/SGAQ%20-%20Análise%20e%20Projeto%20de%20Software.pdf) incluído neste repositório.


## :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE]([.github/LICENSE.md](https://github.com/sidjr2/SGAQ---APS/blob/master/LICENSE)) para mais detalhes.

---

Feito com ♥ by Davi Kreppel, Gustavo Detomi, Leandro Souza, Matheus Nascimento e Sidney Junior. :wave:
