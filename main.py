from typing import List

class User:
    contador = 0
    def __init__(self, origem, destino):
        self.__origem = origem
        self.__destino = destino
        self.__id = User.contador
        User.contador+=1
            
    @property
    def origem(self: object) -> int:
        return self.__origem

    @property
    def destino(self: object) -> int:
        return self.__destino
    
    @property
    def direção(self: object) -> int:
        return self.__direção
    
    @property
    def id(self: object) -> int:
        return self.__id
    
class Elevador:
    contador = 1
    def __init__(self, andar, limite):       
        self.__id = Elevador.contador
        self.__ocupacao: List[User]= []
        self.__capacidade: int = self.old
        self.__dentro: List[User] = []
        self.__atual = andar
        self.__limite = limite
        self.__disp = True
        self.__aux = 0
        Elevador.contador+=1

    @property
    def id(self: object) -> int:
        return self.__id
    
    @property
    def ocupacao(self: object) -> List[User]:
        return self.__ocupacao
    
    @property
    def old(self: object) -> int:
        return self.__capacidade
    
    
    def add(self, pessoa:User):
        self.ocupacao.append(pessoa)
        
