import main

def last():
    elevador: main.Elevador = main.Elevador(0,100)
    print('Olá bem vindo ao sistema de Elevador')
    while input('Tem alguem esperando o elevador ? ') == 'sim':
        nome = input('Diga-me qual o nome do passageiro: ')
        origem = int(input('Diga-me que andar ele(a) está: '))
        destino = int(input('Para qual andar ele(a) deseja ir ? '))
        if origem >= 0 and origem <= 100 or destino <= 100 and destino >= 0:
            pessoa: main.User = main.User(nome,origem,destino)
            elevador.add(pessoa)
        else: print("O elevador não pode ir até esse andar...")
    
    elevador.distancia_do_elevador()
    elevador.levar_elevador()
        
last()

