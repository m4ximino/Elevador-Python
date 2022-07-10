from shutil import move
from turtle import distance
from xmlrpc.client import boolean
from typing import List


shafts = 5
elevadores = 3
class User:
    contador = 0
    def __init__(self, origem, destino):
        self.__origem = origem
        self.__destino = destino
        self.__id = User.contador
        User.contador+=1
        if origem - destino > 0:
            self.__direção = 1
        else:
            self.__direção = -1
            
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
            

# #Predio é composto de andares e fossos de elevador.
# #Cada fosso contem 2 elevadores, um que começa no terreo e outro na cobertura.
# #Os andares tem entradas para os fossos e um numero X de transeuntes a cada momento.
class Predio:
    def __init__(self, size):
        self.size = size
        # self.andares = []
        # self.shaft = []
#         # for i in range(size):
#         #     self.andares.append(Andar(i, self))
#         # for i in range(shafts):
#         #     for j in range(elevadores):
#         #         self.shaft.append(Elevador(self.andares[j*100], i, j))
#     #essa função verifica se existe um elevador no caminho entre o elevador
#     #que vai partir e seu destino, categorizando-o como emperrado.
#     # def stuck(self, shaft):
#     #     if self.shaft[shaft][1].atual < self.shaft[shaft][0].atual + self.shaft[shaft][0].destino:
#     #         return True
#     #     elif self.shaft[shaft][0].atual > self.shaft[shaft][1].atual - self.shaft[shaft][1].destino:
#     #         return True
#     #     else:
#     #         return False
class Andar:
    def __init__(self, numero, predio:Predio) -> None:
        self.numero = numero
        self.predio = predio

class Elevador:
    def __init__(self, andar:Andar):       
        self.ocupacao: int = 0
        self.capacidade: int = 6
        self.destino: Andar = None
        self.locomover: Andar = Andar(0, Predio(300))
        self.atual: Andar = andar
        self.disp = True
        self.k = 0
    
    # Move o elevador até a pessoa
    def ir_ate_passageiro(self, pessoa:User, outras: List[User]):
        if self.locomover.numero < pessoa.origem:
            print(f"Elevador está no piso: ", self.locomover.numero)
            for j in outras:
                 if int(self.locomover.numero) == j.destino:
                        self.move(j.destino, outras)
            self.locomover.numero+=1
            return self.ir_ate_passageiro(pessoa, outras)
        elif self.locomover.numero > pessoa.origem:
            print(f"Elevador está no piso: ", self.locomover.numero)
            for j in outras:
                if int(self.locomover.numero) == int(j.destino):
                    self.move(j.destino, outras)
            self.locomover.numero-=1
            return self.ir_ate_passageiro(pessoa, outras)
        elif self.locomover.numero == pessoa.origem:
            print(f"Pegou passageiro no piso: ", self.locomover.numero)
            for j in outras:
                    if int(self.locomover.numero) == j.destino:
                        self.move(j.destino, outras)
            return outras                
                        

    def distancia_do_elevador(self, destino: List[User]):
        try:
            for i in range(len(destino)):
                for j in range(len(destino)):
                    if abs(self.locomover.numero - destino[i].origem) <= abs(self.locomover.numero - destino[j].origem) and abs(self.locomover.numero - destino[i].origem) != abs(self.locomover.numero - destino[j].origem):
                        aux = destino [i]
                        destino[i] = destino[j]
                        destino[j] = aux
        except TypeError:
            None
 
    # Move o elevador até o destino do passageiro
    def sair(self, pessoas: List[User]):
        outras: List[User] = []
        self.distancia_do_elevador(pessoas)
        self.ocupacao = len(pessoas)
        for i in pessoas:
            self.ir_ate_passageiro(i, outras)
            outras.append(i)
            pessoas = self.distancia_do_elevador(pessoas)
        try:
            if len(outras) > 0 :
                self.distancia_do_elevador(outras)
                for i in outras:
                    print(i.id, i.origem,i.destino)
                    self.move(i.destino, outras)
        except TypeError: None
        # if len(outras) > 0:
        #     for i in outras:
        #         self.move(i.destino, outras)


    def move(self, direcao, outras: List[User]):
        if self.locomover.numero == direcao:
            self.ocupacao-=1
            print(f"Elevador chegou ao seu destino passageiro: ", direcao)
            print(f"Quantidade de passageiros: ", self.ocupacao)
            for j in outras:
                if self.locomover.numero == j.destino:
                    outras.remove(j)
            try:
                return self.move(outras[0].destino, outras)
            except IndexError as erro: return outras 
        elif self.locomover.numero < direcao:
            for j in outras:
                if self.locomover.numero == j.destino:
                    self.move(j.destino, outras)
                    
            print(f"Elevador está no piso: ", self.locomover.numero)
            self.locomover.numero+=1
            self.move(direcao, outras)
        elif self.locomover.numero > direcao:
            for j in outras:
                if self.locomover.numero == j.destino:
                    self.move(j.destino, outras)
            print(f"Elevador está no piso: ", self.locomover.numero)
            self.locomover.numero-=1
            self.move(direcao, outras)
