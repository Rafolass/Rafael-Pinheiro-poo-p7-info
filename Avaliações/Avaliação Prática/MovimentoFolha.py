class MovimentoFolha:
    def __init__(self,colaborador, descricao, valor, tipomovimento):
        self._descricao = descricao
        self._valor = valor
        self._tipomovimento = tipomovimento
        self._colaborador = colaborador
    def getTipo(self):
        return self._tipomovimento

    def getValor(self):
        return self._valor
