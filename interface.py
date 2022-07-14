import main

def last():
    elevador: main.Elevador = main.Elevador(0,100)
    print('Olá bem vindo ao sistema de Elevador')
    while input('Tem alguem esperando o elevador?') != 'sim':
        nome = input()
        origem = int(input())
        destino = int(input())
        if origem >= 0 and origem <= 100 or destino <= 100 and destino >= 0:
            pessoa: main.User = main.User(nome,origem,destino)
            elevador.add(pessoa)
        else: print("O elevador não pode ir até esse andar...")
