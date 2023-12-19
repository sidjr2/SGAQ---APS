class Quadra:
    def __init__(self, nome, local, capacidade, horario_disponivel, horario_limpeza) -> None:
        self.nome = nome
        self.local = local
        self.capacidade = int(capacidade)
        self.horario_disponivel = horario_disponivel
        self.horario_limpeza = horario_limpeza
        pass