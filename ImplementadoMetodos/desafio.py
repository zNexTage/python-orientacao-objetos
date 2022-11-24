'''
    Desafio: para ajudar na formatação de datas você deve criar uma nova classe auxiliar. Essa classe deve representar uma Data (sem hora) que sabe imprimir uma data formatada. Ela deve funcionar dessa forma:
'''

class Data:
    def __init__(self, data, mes, ano):
        self.data = data
        self.mes = mes
        self.ano = ano

    def formatada(self):
        return f'{self.data}/{self.mes}/{self.ano}'

