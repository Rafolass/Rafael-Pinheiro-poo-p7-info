from MovimentoFolha import MovimentoFolha
class Colaborador:
    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salario_atual):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._bairro = bairro
        self._cep = cep
        self._cpf = cpf
        self._salario_atual = salario_atual
        self._lista_movimentos = []
    def getsalario(self):
        return self._salario_atual

    def inserirMovimentoColaborador(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self._lista_movimentos.append(movimento)

    def calcularSalario(self):
        totalprovento = 0
        totaldesconto = 0
        for movimento in self._lista_movimentos:
            if movimento.getTipo().value == 1:
                totalprovento += movimento.getValor()
            else:
                totaldesconto += movimento.getValor()
        SalarioLiquido = self._salario_atual + totalprovento - totaldesconto
        print(f'-------Codigo:{self._codigo}  | Nome:{self._nome}\n --------Salário:R${self._salario_atual:.0f}\n '
              f'--------Total Proventos:R${totalprovento:.0f}\n --------Total Descontos:R${totaldesconto:.0f}\n --------Valor Liquido a Receber:R${SalarioLiquido:.0f}\n')
