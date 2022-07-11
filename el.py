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
        self.id = Elevador.contador
        self.ocupacao: User = []
        self.capacidade: int = len(self.ocupacao)
        self.dentro: int = []
        self.atual = andar
        self.limite = limite
        self.disp = True
        self.aux = 0
        Elevador.contador+=1

    
    def add(self, pessoa:User):
        self.ocupacao.append(pessoa)

    def vizualizar_passageiros(self):
        for i in self.ocupacao:
            print(f"Passeiro: {i.id} Origem: {i.origem} Destino {i.destino} Elevador: {self.id}")
            
    def buscar_passageiro_por_distancia(self):
        if len(self.ocupacao) != None:
            for i in range(len(self.ocupacao)):
                for j in range(len(self.ocupacao)):
                    if abs(self.atual- self.ocupacao[i].origem) <= abs(self.atual - self.ocupacao[j].origem):
                        aux = self.ocupacao [i]
                        self.ocupacao[i] = self.ocupacao[j]
                        self.ocupacao[j] = aux
            
def sincronia(elevador1:Elevador, elevador2:Elevador, elevador3: Elevador):
    try:
        if elevador1.atual < elevador1.ocupacao[0].origem or elevador2.atual < elevador2.ocupacao[0].origem or elevador2.atual < elevador2.ocupacao[0].origem:
            print(f"Elevador : {elevador1.id} está no piso: {elevador1.atual}")
            for i in elevador1.ocupacao:
                if elevador1.atual == i.origem:
                    print(f"Elevador : {elevador1.id} pegou passageiro no piso : {elevador1.atual}")
                    elevador1.ocupacao.remove(i)
            elevador1.atual+=1
            print(f"Elevador : {elevador2.id} está no piso: {elevador2.atual}")
            for i in elevador2.ocupacao:
                if elevador2.atual == i.origem:
                    print(f"Elevador : {elevador2.id} pegou passageiro no piso : {elevador2.atual}")
                    elevador2.ocupacao.remove(i)
            elevador2.atual+=1
            print(f"Elevador : {elevador3.id} está no piso: {elevador3.atual}")
            for i in elevador3.ocupacao:
                if elevador3.atual == i.origem:
                    print(f"Elevador : {elevador3.id} pegou passageiro no piso : {elevador3.atual}")
                    elevador3.ocupacao.remove(i)
            elevador3.atual+=1
            return sincronia(elevador1, elevador2, elevador3)
        elif elevador1.atual > elevador1.ocupacao[0].origem or elevador2.atual > elevador2.ocupacao[0].origem or elevador3.atual > elevador3.ocupacao[0].origem:
            print(f"Elevador : {elevador1.id} está no piso: {elevador1.atual}")
            for i in elevador1.ocupacao:
                if elevador1.atual == i.origem:
                    print(f"Elevador : {elevador1.id} pegou passageiro no piso : {elevador1.atual}")
                    elevador1.ocupacao.remove(i)
            elevador1.atual-=1
            print(f"Elevador : {elevador2.id} está no piso: {elevador2.atual}")
            for i in elevador2.ocupacao:
                if elevador2.atual == i.origem:
                    print(f"Elevador : {elevador2.id} pegou passageiro no piso : {elevador2.atual}")
                    elevador2.ocupacao.remove(i)
            elevador2.atual-=1
            print(f"Elevador : {elevador3.id} pegou passageiro no piso : {elevador3.atual}")
            elevador3.ocupacao.remove(elevador1.ocupacao[0])
            for i in elevador3.ocupacao:
                if elevador3.atual == i.origem:
                    print(f"Elevador : {elevador3.id} pegou passageiro no piso : {elevador3.atual}")
                    elevador3.ocupacao.remove(i)
            return sincronia(elevador1, elevador2, elevador3)
        elif elevador1.atual == elevador1.ocupacao[0].origem:
            print(f"Elevador : {elevador1.id} pegou passageiro no piso : {elevador1.atual}")
            elevador1.ocupacao.remove(elevador1.ocupacao[0])
            for i in elevador1.ocupacao:
                if elevador1.atual == i.origem:
                    print(f"Elevador : {elevador1.id} pegou passageiro no piso : {elevador1.atual}")
                    elevador1.ocupacao.remove(i)
            print(f"Elevador : {elevador2.id} pegou passageiro no piso : {elevador2.atual}")
            elevador2.ocupacao.remove(elevador2.ocupacao[0])
            for i in elevador2.ocupacao:
                if elevador2.atual == i.origem:
                    print(f"Elevador : {elevador2.id} pegou passageiro no piso : {elevador2.atual}")
                    elevador2.ocupacao.remove(i)
            print(f"Elevador : {elevador3.id} pegou passageiro no piso : {elevador3.atual}")
            elevador3.ocupacao.remove(elevador1.ocupacao[0])
            for i in elevador3.ocupacao:
                if elevador3.atual == i.origem:
                    print(f"Elevador : {elevador3.id} pegou passageiro no piso : {elevador3.atual}")
                    elevador3.ocupacao.remove(i)
    except IndexError and ValueError and IndexError: 
        None
    
    # try:
    #     if elevador2.atual < elevador2.ocupacao[0].origem:
    #         for i in elevador2.ocupacao:
    #             if elevador2.atual == i.origem:
    #                 print(f"Elevador : {elevador2.id} pegou passageiro no piso : {elevador2.atual}")
    #                 elevador2.ocupacao.remove(i)
    #         print(f"Elevador : {elevador2.id} está no piso: {elevador2.atual}")
    #         elevador2.atual+=1
    #         return sincronia(elevador1, elevador2, elevador3)
    #     elif elevador2.atual > elevador2.ocupacao[0].origem:
    #         print(f"Elevador : {elevador2.id} está no piso: {elevador2.atual}")
    #         for i in elevador2.ocupacao:
    #             if elevador2.atual == i.origem:
    #                 print(f"Elevador : {elevador2.id} pegou passageiro no piso : {elevador2.atual}")
    #                 elevador2.ocupacao.remove(i)
    #         elevador2.atual-=1
    #         return sincronia(elevador1, elevador2, elevador3)
    #     elif elevador2.atual == elevador2.ocupacao[0].origem:
    #         print(f"Elevador : {elevador2.id} pegou passageiro no piso : {elevador2.atual}")
    #         elevador2.ocupacao.remove(elevador2.ocupacao[0])
    #         for i in elevador2.ocupacao:
    #             if elevador2.atual == i.origem:
    #                 print(f"Elevador : {elevador2.id} pegou passageiro no piso : {elevador2.atual}")
    #                 elevador2.ocupacao.remove(i)
    # except IndexError and ValueError and IndexError: 
    #     None
  
                    
                    
                    
    # try:
    #     if elevador3.atual < elevador3.ocupacao[0].origem:
    #         for i in elevador3.ocupacao:
    #             if elevador3.atual == i.origem:
    #                 print(f"Elevador : {elevador3.id} pegou passageiro no piso : {elevador3.atual}")
    #                 elevador3.ocupacao.remove(i)
    #         print(f"Elevador : {elevador3.id} está no piso: {elevador3.atual}")
    #         elevador3.atual+=1
    #         return sincronia(elevador1, elevador2, elevador3)
    #     elif elevador3.atual > elevador3.ocupacao[0].origem:
    #         for i in elevador3.ocupacao:
    #             if elevador3.atual == i.origem:
    #                 print(f"Elevador : {elevador3.id} pegou passageiro no piso : {elevador3.atual}")
    #                 elevador3.ocupacao.remove(i)
    #         print(f"Elevador : {elevador3.id} está no piso: {elevador3.atual}")
    #         elevador3.atual-=1
    #         return sincronia(elevador1, elevador2, elevador3)
    #     elif elevador3.atual == elevador3.ocupacao[0].origem: 
    #         print(f"Elevador : {elevador3.id} pegou passageiro no piso : {elevador3.atual}")
    #         elevador3.ocupacao.remove(elevador1.ocupacao[0])
    #         for i in elevador3.ocupacao:
    #             if elevador3.atual == i.origem:
    #                 print(f"Elevador : {elevador3.id} pegou passageiro no piso : {elevador3.atual}")
    #                 elevador3.ocupacao.remove(i)
    # except IndexError and ValueError and IndexError: 
    #     None
    
