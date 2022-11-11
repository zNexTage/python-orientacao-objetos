def criar_conta(numero, titular, saldo, limite):
    return {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite
    }

def depositar(conta, valor):
    conta['saldo'] += valor


def sacar(conta, valor):
    conta['saldo'] -= valor

def gerar_extrato(conta):
    print(f""""
        Titular: {conta['titular']}
        Número: {conta['numero']}
        Saldo é {conta['saldo']}

    """)

