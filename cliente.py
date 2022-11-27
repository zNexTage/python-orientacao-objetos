class Cliente:
    def __init__(self, nome:str) -> None:
        self.__nome = nome
    
    @property
    def nome(self):        
        ''' get nome '''

        return self.__nome.title()
    
    @nome.setter
    def nome(self, nome):
        ''' set nome '''

        self.__nome = nome
