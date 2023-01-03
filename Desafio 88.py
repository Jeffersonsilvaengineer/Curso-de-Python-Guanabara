'''Crie um programa que ajude um jogador da mega sena a criar palpites, O programa vai perguntar quantos
jogos serão gerados e quantos números entre 6 e 20 serão sorteados por jogo,o programa sorteará números entre 1 e 60
 para cada jogo, cadastrando tudo em uma lista composta.'''

import random
from time import sleep
print('---' * 20)
print('{: ^60}'.format('LOTERIAS FLORA NECTAR'))
print('---'*20)
xy = str(input('DESEJA JOGAR ->[MEGA SENA / QUINA]: ')).upper()
print('---'*20)
if xy == 'MEGA SENA':
    print('{: ^60}'.format('BOLÃO MEGA SENA'))
    print('---' * 20)
    jogos = int(input('QUANTOS JOGOS VOCÊ DESEJA FAZER: '))
    print('---'*20)
    quantidade = int(input('QUANTOS NÚMEROS POR JOGO VOCÊ DESEJA? ESCOLHA ENTRE [06 E 20]: '))
    print('=-=' * 20)
    print('{: ^40}'.format(f'SORTEANDO {jogos} JOGOS COM {quantidade} NÚMEROS POR JOGO!'))
    print('=-='*20)
    valor = 0
    for c in range(jogos):
        list_mega = []
        while True:
            numeros = random.randint(1, 60)
            if numeros in list_mega:
                continue
            else:
                list_mega.append(numeros)
            list_mega.sort()
            if len(list_mega) == quantidade:
                    break
        sleep(0.5)
        print(f'{c+1:>2}º JOGO --> {list_mega}')
    print('=-=' * 20)
    if len(list_mega) == 6:
        valor = 4.5 * jogos
    elif len(list_mega) == 7:
        valor = 31.5 * jogos
    elif len(list_mega) == 8:
        valor = 126 * jogos
    elif len(list_mega) == 9:
        valor = 378 * jogos
    elif len(list_mega) == 10:
        valor = 945 * jogos
    elif len(list_mega) == 11:
        valor = 2079 * jogos
    elif len(list_mega) == 12:
        valor = 4158 * jogos
    elif len(list_mega) == 13:
        valor = 7722 * jogos
    elif len(list_mega) == 14:
        valor = 13513.50 * jogos
    elif len(list_mega) == 15:
        valor = 22522.50 * jogos
    elif len(list_mega) == 16:
        valor = 36036 * jogos
    elif len(list_mega) == 17:
        valor = 55692 * jogos
    elif len(list_mega) == 18:
        valor = 83538 * jogos
    elif len(list_mega) == 19:
        valor = 122094 * jogos
    elif len(list_mega) == 20:
        valor = 174420 * jogos
    print(f'O VALOR TOTAL DESTE BOLÃO É R$ {valor :0,} REAIS')
elif xy == 'QUINA':
    print('{: ^60}'.format('BOLÃO DA QUINA'))
    print('---' * 20)
    jogos = int(input('QUANTOS JOGOS VOCÊ DESEJA FAZER: '))
    print('---' * 20)
    quantidade = int(input('QUANTOS NÚMEROS POR JOGO VOCÊ DESEJA? ESCOLHA ENTRE [05 E 15]: '))
    print('=-=' * 20)
    print('{: ^40}'.format(f'SORTEANDO {jogos} JOGOS COM {quantidade} NÚMEROS POR JOGO!'))
    print('=-=' * 20)
    valor = 0
    for c in range(jogos):
        list_quina = []
        while True:
            numeros = random.randint(1, 80)
            if numeros in list_quina:
                continue
            else:
                list_quina.append(numeros)
            list_quina.sort()
            if len(list_quina) == quantidade:
                break
        sleep(0.5)
        print(f'{c + 1:>2}º JOGO --> {list_quina}')
    print('=-=' * 20)
    if len(list_quina) == 5:
        valor = 2 * jogos
    elif len(list_quina) == 6:
        valor = 12 * jogos
    elif len(list_quina) == 7:
        valor = 42 * jogos
    elif len(list_quina) == 8:
        valor = 112 * jogos
    elif len(list_quina) == 9:
        valor = 252 * jogos
    elif len(list_quina) == 10:
        valor = 504 * jogos
    elif len(list_quina) == 11:
        valor = 924 * jogos
    elif len(list_quina) == 12:
        valor = 1584 * jogos
    elif len(list_quina) == 13:
        valor = 2574 * jogos
    elif len(list_quina) == 14:
        valor = 4004 * jogos
    elif len(list_quina) == 15:
        valor = 6006 * jogos
    print(f'O VALOR TOTAL DESTE BOLÃO É R$ {valor :0,} REAIS')
    
