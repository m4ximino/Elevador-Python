from matplotlib import use
import elevadores
users = []
predio = elevadores.Predio(300)
andar = elevadores.Andar(0,predio)


# elevador = elevadores.Elevador(andar)
while input("Digite se deseja entrar no elevador: ") == 's':
    origem = int(input("digite onde está: "))
    destino = int(input("digite para onde quer ir: "))
    users.append(elevadores.User(origem, destino))

for i in range(len(users)):
    for j in range(len(users)):
        if users[i].origem < users[j].origem:
            aux = users[i]
            users[i] = users[j]
            users[j] = aux
        
for i in users:
    print(i.origem, i.destino, i.direção)
elevador1 = elevadores.Elevador(elevadores.Andar(i.origem,predio))


elevador2 = elevadores.Elevador(elevadores.Andar(100,predio))
elevador3 = elevadores.Elevador(elevadores.Andar(200,predio))

# entrar no elevador
elevador1.sair(users)
