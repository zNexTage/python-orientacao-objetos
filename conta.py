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

    def sacar(self, valor) -> None:
        if valor > self.__limite:
            raise ValueError(f'O limite de saque disponível é: {self.__limite}')

        self.__saldo -= valor

    @property
    def titular(self):
        return self.__titular

    def transferir(self, valor, contaDestino):
        self.sacar(valor)

        contaDestino.depositar(valor)

        print(f'{self.__titular} transferiu R$ {valor} para {contaDestino.titular}')


