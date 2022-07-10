import elevadores
from typing import List


andar: elevadores.Andar = elevadores.Andar(0,elevadores.Predio(300))
pessoa2: elevadores.User = elevadores.User(1, 5)
pessoa1: elevadores.User = elevadores.User(2, 5)
pessoa4: elevadores.User = elevadores.User(3, 15)
pessoa: elevadores.User = elevadores.User(4, 2)
pessoa3: elevadores.User = elevadores.User(13, 4)
pessoa5: elevadores.User = elevadores.User(101, 7)
pessoa6: elevadores.User = elevadores.User(100, 49)

listpessoas: List[elevadores.User] = []
listpessoas.append(pessoa)
listpessoas.append(pessoa1)
listpessoas.append(pessoa2)
listpessoas.append(pessoa3)
listpessoas.append(pessoa4)
listpessoas.append(pessoa5)
listpessoas.append(pessoa6)


el : elevadores.Elevador = elevadores.Elevador(andar)
# print(el.ir_ate_passageiro())
elevadores.Elevador.sair(el,listpessoas)
aux =0
# for i in listpessoas:
#     aux+=1
#     print("O Proximo é:", listpessoas[aux+1].origem)
