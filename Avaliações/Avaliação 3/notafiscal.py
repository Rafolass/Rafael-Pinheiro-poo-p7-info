"""
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado.
"""
import datetime
from cliente import Cliente
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.datetime.now()
        self._itens = []
        self._valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def dataNota(self):
        listadatahora = str(self._data).split()
        DataLista = listadatahora[0].split('-')
        UltimaData = f'{DataLista[2]}/{DataLista[1]}/{DataLista[0]}'
        return UltimaData

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self._valorNota = valor

    def getValor(self):
        return self._valorNota

    def imprimirNotaFiscal(self):
        traco = '-' * 111

        finalNotaFormatada = ''

        if len(self._itens) > 0:
            for item in self._itens:
                finalNotaFormatada += f'\n\n{item.getSequencial()}{" " * 3}{item.getDescricao()}'
                finalNotaFormatada += ' ' * (60 - len(item.getDescricao()))
                finalNotaFormatada += '{:.2f}             {:.2f}                  {:.2f}'.format(
                    item.getQuantidadeProduto(), item.getValorUnitario(),
                    item.getValorItem())

        finalNotaFormatada += '\n{}\nValor Total: {:.2f}'.format(traco, self._valorNota)

        print(traco)
        print(f'NOTA FISCAL{" " * 90}{self.dataNota()}')
        print(f'Cliente:{self._cliente.getCodigoCliente()}{" " * 6}{" " * 4}Nome:{self._cliente.getNomeCliente()}')
        print(f'CPF/CNPJ: {self._cliente.getCnpjCpf()}')
        print(traco)
        print('ITENS')
        print(traco)
        print(f'Seq{" " * 3}Descrição{" " * 52}QTD{" " * 7}Valor Unit{" " * 19}Preço')
        print(f'{"-" * 4}  {"-" * 56}  {"-" * 7}   {"-" * 15}  {"-" * 21}')
        print(finalNotaFormatada)
