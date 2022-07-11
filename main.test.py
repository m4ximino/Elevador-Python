import main
from typing import List

elevador1: main.Elevador = main.Elevador(0, 100)


pessoa: main.User = main.User(4, 2)
pessoa1: main.User = main.User(2, 5)
pessoa2: main.User = main.User(1, 5)
pessoa3: main.User = main.User(13, 4)
# pessoa9: main.User = main.User(100, 49)
pessoa4: main.User = main.User(3, 15)
pessoa5: main.User = main.User(6, 7)
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


print(len(elevador1.ocupacao))

for i in elevador1.ocupacao:
    print(i.id, i.origem, i.destino)

# elevador1.old
    
print(elevador1.capacidade)