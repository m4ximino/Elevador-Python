from typing import List
subir = 1
descer = 0
class User:
    def __init__(self, nome,origem, destino):
        self.__origem = origem
        self.__destino = destino
        self.__id: str = nome
            
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
    def id(self: object) -> str:
        return self.__id
    
class Elevador:
    contador=1
    def __init__(self, andar, limite):       
        self.__id = Elevador.contador
        self.__esperando: List[User]= []
        self.__capacidade: int = 0
        self.__dentro: List[User] = []
        self.atual = andar
        self.__limite = limite
        self.__disp = True
        self.__aux = 0
        Elevador.contador+=1

    @property
    def id(self: object) -> int:
        return self.__id
    
    @property
    def esperando(self: object) -> List[User]:
        return self.__esperando
    
    @property
    def capacidade(self: object) -> int:
        return self.__capacidade
    
    @property
    def dentro(self: object) -> List[User]:
        return self.__dentro
    
    def add(self, pessoa:User):
        self.esperando.append(pessoa)
            
    def distancia_do_elevador(self):
        try:
            for i in range(len(self.esperando)):
                for j in range(len(self.esperando)):
                    if abs(self.atual - self.esperando[i].origem) <= abs(self.atual- self.esperando[j].origem) and abs(self.atual- self.esperando[i].origem) != abs(self.atual- self.esperando[j].origem):
                        aux = self.esperando [i]
                        self.esperando[i] = self.esperando[j]
                        self.esperando[j] = aux
        except TypeError:
            None
            
    def levar_elevador(self):
        try:
            if self.atual == self.esperando[0].origem:
                print(f"Elevador pegou passageiro : {self.esperando[0].id}")
                self.dentro.append(self.esperando[0])
                self.esperando.remove(self.esperando[0])
                self.levar_passageiro()
                self.levar_elevador()
            elif self.atual < self.esperando[0].origem:
                self.move_elevador(subir)
                self.levar_elevador()
            else:
                self.move_elevador(descer)
                self.levar_elevador()
        except IndexError: None
    
    def levar_passageiro(self):
        if self.atual == self.dentro[0].destino:
                print(f"Elevador chegou no destino de : {self.dentro[0].id}")
                self.dentro.remove(self.dentro[0])
        elif self.atual < self.dentro[0].destino:
                self.move_elevador(subir)
                self.levar_passageiro()
        elif self.atual > self.dentro[0].destino:
                self.move_elevador(descer)
                self.levar_passageiro()  
    
    def move_elevador(self, direcao: int):
        if direcao == 1:
            print(f"Elevador está no piso : {self.atual}")
            self.vereficar_piso()
            self.atual+=1
        else:
            print(f"Elevador está no piso : {self.atual}")
            self.vereficar_piso()
            self.atual-=1
            
    def vereficar_piso(self):
        for i in self.esperando:
            if self.atual==i.origem:
                print(f"Elevador pegou passageiro : {i.id}")
                self.dentro.append(self.esperando[0])
                self.esperando.remove(self.esperando[0])
                # self.capacidade+=1
        for i in self.dentro:
            if self.atual == i.destino:
                print(f"Elevadou chegou no destino de : {i.id}")
                self.dentro.remove(i)
                # self.capacidade-=1
            
            
        
