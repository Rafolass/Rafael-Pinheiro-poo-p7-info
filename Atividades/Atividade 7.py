class Cliente:
    def __init__(self, nome, telefone, problema, listconsultas):
        self.nome = nome
        self.telefone = telefone
        self.problema = problema
        self.listconsultas = listconsultas

    def set_planodesaude(self, planodesaude):
        self.planodesaude = planodesaude

    def __int__(self, planodesaude):
        self.planodesaude = planodesaude

class Data:
    def set_data(self, dia):
        self.dia = dia

    def set_hora(self, hora):
        self.hora = hora
    def __init__(self, dia, hora) :
        self.dia = dia
        self.hora = hora

class Medico:
    def __init__(self, nome, especializacao, telefone, listconsultas):
        self.nome = nome
        self.especializacao = especializacao
        self.telefone = telefone
        self.listconsultas = listconsultas

class Consult:
    def get_Data(self):
        return self.data
    def get_Medico(self):
        return self.medico
    def get_Cliente(self):
        return self.cliente
