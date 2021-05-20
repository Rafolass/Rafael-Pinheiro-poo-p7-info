from MovimentoFolha import MovimentoFolha
class FolhaPagamento:
    def __init__(self, mes, ano, totalproventos, totaldescontos):
        self._mes = mes
        self._totaldescontos = totaldescontos
        self._totalproventos = totalproventos
        self._ano = ano
        self._listamovimentos = []
        self._colaboradores = []

    def inserirmovimentoFP(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self._listamovimentos.append(movimento)

    def total_salario(self):
        total_salario = 0
        for colaborador in self._colaboradores:
            total_salario += colaborador
        return total_salario


    def calcularfolha(self):
        for  movimento in self._listamovimentos:
            if movimento.getTipo().value == 1:
                self._totalproventos += movimento.getValor()
            else:
                self._totaldescontos += movimento.getValor()
        totalpagar = (self.total_salario() + self._totalproventos) - self._totaldescontos
        print(f' --------Total de Salários= R${self.total_salario():.0f}\n --------Total de Proventos = R${self._totalproventos:.0f}\n '
              f'--------Total de Descontos = R${self._totaldescontos:.0f}\n --------Total a Pagar = R${totalpagar:.0f}\n')

    def setColaborador(self, colaborador):
        self._colaboradores.append(colaborador.getsalario())
