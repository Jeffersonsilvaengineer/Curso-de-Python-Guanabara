'''Refaça o desafio 28 de forma melhorada, onde o computador vai pensar em um numero entre 0 e 10, e o jogador
vai jogar até acertar, mostrando no final quantos palpites foram necessários para o acerto! '''

import random
jogador = 0
tentativas = 0
computador = random.randint(0, 1000000)
while jogador != computador:
    jogador = int(input('Digite um número: '))
    tentativas += 1
    if jogador == computador:
        jogador = computador
    else:
        if jogador > computador:
            print('MENOS...')
        elif jogador < computador:
                    print('MAIS...')
print(f'PARABÉNS!, você acertou o número pensado pelo computador depois de {tentativas} tentativas! ')
