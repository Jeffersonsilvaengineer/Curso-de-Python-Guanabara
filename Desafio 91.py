'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador 1:': randint(1, 6),
             'Jogador 2:': randint(1, 6),
             'Jogador 3:': randint(1, 6),
             'Jogador 4:': randint(1, 6)}
print('<<< JOGANDO O DADO >>>')
for k, v in jogadores.items():
    sleep(0.5)
    print(f'{k} jogou o dado e tirou {v}')
print('=-' * 20)
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('<<< ORDEM CLASSIFICATÓRIA >>>')
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'{i + 1}º LUGAR: {v[0]} COM {v[1]}')
