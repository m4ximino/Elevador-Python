import elevador
from typing import List

elevador1: elevador.Elevador = elevador.Elevador(10, 100)


pessoa: elevador.User = elevador.User("João",4, 2)
pessoa1: elevador.User = elevador.User("Adriana",2, 5)
pessoa2: elevador.User = elevador.User("Marcos",1, 5)
pessoa3: elevador.User = elevador.User("Ivan",13, 4)
# pessoa9: elevador.User = elevador.User(,100, 49)
pessoa4: elevador.User = elevador.User("Lucas",3, 15)
pessoa5: elevador.User = elevador.User("Geremias",6, 7)
# pessoa6: elevador.User = elevador.User(100, 49)
# pessoa10: elevador.User = elevador.User(100, 49)
# pessoa8: elevador.User = elevador.User(134, 90)

listpessoas: List[elevador.User] = []
listpessoas.append(pessoa)
listpessoas.append(pessoa1)
listpessoas.append(pessoa2)
listpessoas.append(pessoa3)
listpessoas.append(pessoa4)
listpessoas.append(pessoa5)
# listpessoas.append(pessoa6)
# listpessoas.append(pessoa7)
# listpessoas.append(pessoa8)


for i in listpessoas:
    elevador1.add(i)

# elevador1.capacidade = len(elevador1.ocupacao)


elevador1.distancia_do_elevador()

for i in elevador1.esperando:
    print(i.id, "Origem:",i.origem, "Destino:",i.destino)
    
elevador1.levar_elevador()


for i in elevador1.esperando:
    print(i.id, "Origem:",i.origem, "Destino:",i.destino)
    

for i in elevador1.dentro:
    print(i.id, "Origem:",i.origem, "Destino:",i.destino)