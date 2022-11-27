class Conta:
    def __init__(self, numero, titular, saldo, limite) -> None:
        print(f'Construindo objeto... {self}')
	    
        # Private attributes
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self) -> None:
        print(f'Saldo de  R$ {self.__saldo} do titular {self.__titular}')

    def depositar(self, valor) -> None:
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        valor_disponivel_saque = self.__saldo + self.__limite

        return valor_saque <= valor_disponivel_saque

    def sacar(self, valor) -> None:
        if not self.__pode_sacar(valor):
            print(f'O limite de saque disponível é: {self.__limite}')

        self.__saldo -= valor

    @property
    def titular(self):
        return self.__titular

    def transferir(self, valor, contaDestino):
        self.sacar(valor)

        contaDestino.depositar(valor)

        print(f'{self.__titular} transferiu R$ {valor} para {contaDestino.titular}')

    @staticmethod
    def codigo_banco():
        ''' class method '''
        
        return "001"

