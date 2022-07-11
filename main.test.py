import main
from typing import List

elevador1: main.Elevador = main.Elevador(10, 100)


pessoa: main.User = main.User("João",4, 2)
pessoa1: main.User = main.User("Adriana",2, 5)
pessoa2: main.User = main.User("Marcos",1, 5)
pessoa3: main.User = main.User("Ivan",13, 4)
# pessoa9: main.User = main.User(,100, 49)
pessoa4: main.User = main.User("Lucas",3, 15)
pessoa5: main.User = main.User("Geremias",6, 7)
# pessoa6: main.User = main.User(100, 49)
# pessoa10: main.User = main.User(100, 49)
# pessoa8: main.User = main.User(134, 90)

listpessoas: List[main.User] = []
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

for i in elevador1.dentro:
    print(i.id, "Origem:",i.origem, "Destino:",i.destino)