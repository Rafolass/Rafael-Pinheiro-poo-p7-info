from FolhaPagamento import FolhaPagamento
from Colaborador import Colaborador
from MovimentoFolha import MovimentoFolha
from TipoMovimento import TipoMovimento


def main():

    fp = FolhaPagamento(9, 2019, 0, 0)

    cl01 = Colaborador("100", "Manoel Claudino", "Av 13 de Maio 2081", "88671020",
                      "Benfica", "60020-060", "124543556-89", 4500.00)
    cl02 = Colaborador("200", "Carmelina da Silva", "Avenida dos Expedicionários 1200",
                       "3035-1280", "Aeroporto", "60530-020", "301789435-54",
                       2500.00)
    cl03 = Colaborador("300", "Gurmelina Castro Saraiva", "Av João Pessoa 1020",
                       "3235-1089", "Damas", "60330-090", "350245632-76", 3000.00)

    mf01 = MovimentoFolha(cl01, "Gratificação", 4500.00, TipoMovimento.PROVENTO)
    mf02 = MovimentoFolha(cl01, "Plano Saúde", 1000.00, TipoMovimento.PROVENTO)
    mf03 = MovimentoFolha(cl01, "Pensão", 600.00, TipoMovimento.DESCONTO)
    mf04 = MovimentoFolha(cl02, "Gratificação", 2500.00, TipoMovimento.PROVENTO)
    mf05 = MovimentoFolha(cl02, "Gratificação", 1000.00, TipoMovimento.PROVENTO)
    mf06 = MovimentoFolha(cl02, "Faltas", 600.00, TipoMovimento.DESCONTO)
    mf07 = MovimentoFolha(cl03, "Gratificação", 4500.00, TipoMovimento.PROVENTO)
    mf08 = MovimentoFolha(cl03, "Plano Saúde", 1000.00, TipoMovimento.PROVENTO)
    mf09 = MovimentoFolha(cl03, "Pensão", 600.00, TipoMovimento.DESCONTO)

    fp.setColaborador(cl01)
    fp.setColaborador(cl02)
    fp.setColaborador(cl03)

    fp.inserirmovimentoFP(mf01)
    fp.inserirmovimentoFP(mf02)
    fp.inserirmovimentoFP(mf03)
    fp.inserirmovimentoFP(mf04)
    fp.inserirmovimentoFP(mf05)
    fp.inserirmovimentoFP(mf06)
    fp.inserirmovimentoFP(mf07)
    fp.inserirmovimentoFP(mf08)
    fp.inserirmovimentoFP(mf09)

    cl01.inserirMovimentoColaborador(mf01)
    cl01.inserirMovimentoColaborador(mf02)
    cl01.inserirMovimentoColaborador(mf03)
    cl02.inserirMovimentoColaborador(mf04)
    cl02.inserirMovimentoColaborador(mf05)
    cl02.inserirMovimentoColaborador(mf06)
    cl03.inserirMovimentoColaborador(mf07)
    cl03.inserirMovimentoColaborador(mf08)
    cl03.inserirMovimentoColaborador(mf09)

    print('''Opções para a visualização da folha de pagamento:
            1) Visualizar somente o  primeiro Colaborador:
            2) Visualizar somente o segundo Colaborador:
            3) Visualizar somente o terceiro Colaborador:
            4) Visualizar todos os Colaboradores:
            5) Visualizar o cálculo da Folha:
            0) Para Acabar sua Visualização!
            ''')
    while True:
        opcao = int(input('Digite o que deseja observar: '))
        if opcao == 1:
            cl01.calcularSalario()
        elif opcao == 2:
            cl02.calcularSalario()
        elif opcao == 3:
            cl03.calcularSalario()
        elif opcao == 4:
            cl01.calcularSalario()
            cl02.calcularSalario()
            cl03.calcularSalario()
        elif opcao == 5:
            fp.calcularfolha()
        elif opcao == 0:
            break
        else:
            print('Tente outro valor')


if __name__ == '__main__':
    main()
