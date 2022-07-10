from typing import List
import el

elevador1: el.Elevador = el.Elevador(3, 100)
elevador2: el.Elevador = el.Elevador(101, 200)
elevador3: el.Elevador = el.Elevador(201, 300)

pessoa: el.User = el.User(4, 2)
pessoa1: el.User = el.User(2, 5)
pessoa2: el.User = el.User(1, 5)
pessoa3: el.User = el.User(13, 4)
pessoa9: el.User = el.User(100, 49)
pessoa4: el.User = el.User(3, 15)
pessoa5: el.User = el.User(6, 7)
pessoa6: el.User = el.User(100, 49)
pessoa10: el.User = el.User(100, 49)
pessoa8: el.User = el.User(134, 90)
# pessoa7: el.User = el.User(236, 123)
# pessoa11: el.User = el.User(245, 123)



listpessoas: List[el.User] = []
listpessoas.append(pessoa)
listpessoas.append(pessoa1)
listpessoas.append(pessoa2)
listpessoas.append(pessoa3)
listpessoas.append(pessoa4)
listpessoas.append(pessoa5)
listpessoas.append(pessoa6)
# listpessoas.append(pessoa7)
listpessoas.append(pessoa8)
listpessoas.append(pessoa9)
listpessoas.append(pessoa10)
# listpessoas.append(pessoa11)



for i in listpessoas:
    if i.origem < elevador1.limite: elevador1.add(i)
    elif i.origem > elevador1.limite and i.origem<elevador2.limite: elevador2.add(i)
    # elif i.origem > elevador2.limite and i.origem <elevador3.limite: elevador3.add(i)

elevador1.vizualizar_passageiros()
elevador2.vizualizar_passageiros()
elevador3.vizualizar_passageiros()


el.sincronia(elevador1,elevador2, elevador3)

# elevador1.buscar_passageiro_por_distancia()
# elevador2.buscar_passageiro_por_distancia()
# elevador3.buscar_passageiro_por_distancia()


# elevador1.vizualizar_passageiros()
# elevador2.vizualizar_passageiros()
# elevador3.vizualizar_passageiros()

