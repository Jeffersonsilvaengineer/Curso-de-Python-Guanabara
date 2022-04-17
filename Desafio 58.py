'''Refaça o desafio 28 de forma melhorada, onde o computador vai pensar em um numero entre 0 e 10, e o jogador
vai jogar até acertar, mostrando no final quantos palpites foram necessários para o acerto! '''

import random
jogador = 0
tente = 0
computador = random.randint(0,10)
while jogador != computador:
    jogador = int(input('Digite um número!'))
    tente += 1
    if jogador == computador:
        jogador = computador
    else:
        if jogador > computador:
            print('MENOS...')
        elif jogador < computador:
                    print('MAIS...')
print('PARABÉNS!, você acertou o número pensado pelo computador depois de {} tentativas! '.format(tente))




