import elevadores
from typing import List


andar: elevadores.Andar = elevadores.Andar(0,elevadores.Predio(300))
andar2: elevadores.Andar = elevadores.Andar(100,elevadores.Predio(300))

pessoa2: elevadores.User = elevadores.User(1, 5)
pessoa1: elevadores.User = elevadores.User(2, 5)
pessoa4: elevadores.User = elevadores.User(3, 15)
pessoa: elevadores.User = elevadores.User(4, 2)
pessoa3: elevadores.User = elevadores.User(13, 4)
# pessoa5: elevadores.User = elevadores.User(101, 7)
# pessoa6: elevadores.User = elevadores.User(100, 49)
pessoa6: elevadores.User = elevadores.User(100, 49)
pessoa10: elevadores.User = elevadores.User(100, 49)
pessoa8: elevadores.User = elevadores.User(134, 90)

listpessoas: List[elevadores.User] = []
listpessoas.append(pessoa)
listpessoas.append(pessoa1)
listpessoas.append(pessoa2)
listpessoas.append(pessoa3)
listpessoas.append(pessoa4)
lista2: List[elevadores.User] = []
lista2.append(pessoa6)
lista2.append(pessoa10)
lista2.append(pessoa8)

# listpessoas.append(pessoa5)
# listpessoas.append(pessoa6)


el : elevadores.Elevador = elevadores.Elevador(andar)
el2 : elevadores.Elevador = elevadores.Elevador(andar2)

# print(el.ir_ate_passageiro())
elevadores.Elevador.sair(el,listpessoas)
elevadores.Elevador.sair(el2,lista2)
aux =0
# for i in listpessoas:
#     aux+=1
#     print("O Proximo é:", listpessoas[aux+1].origem)
