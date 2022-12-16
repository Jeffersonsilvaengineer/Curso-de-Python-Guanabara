'''Crie um programa que ajude um jogador da mega sena a criar palpites, O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo cadastrando tudo em uma lista composta.'''
import random
from time import sleep
print('---' * 14)
print('{: ^40}'.format('BOLÃO DA MEGA SENA'))
print('---'*14)
jogos = int(input('Quantos jogos você deseja? '))
print('=-=' * 14)
print('{: ^40}'.format(f'SORTEANDO {jogos} JOGOS'))
print('=-='*14)
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
        if len(list_mega) == 6:
                break
    sleep(0.5)
    print(f'{c+1}º JOGO ---> {list_mega}')
print('=-=' * 14)
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
