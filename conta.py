class Conta:
    def __init__(self, numero, titular, saldo, limite) -> None:
        print(f'Construindo objeto... {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self) -> None:
        print(f'Saldo de  R$ {self.saldo} do titular {self.titular}')

    def depositar(self, valor) -> None:
        self.saldo += valor

    def sacar(self, valor) -> None:
        if valor > self.limite:
            raise ValueError(f'O limite de saque disponível é: {self.limite}')
        
        self.saldo -= valor
            
