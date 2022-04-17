'''Faça um programa que pergunte a idade de 7 pessoas e mostre na tela quantas pessoas ainda não atingiu a
maioridade e quantas já são maiores : considere 21 anos para maioridade!'''

maior = 0
menor = 0
import datetime
for nasc in range(1, 8):
    ano = int(input('O ANO DE NASCIMENTO DA {} PESSOA É? '.format(nasc)))
    atual = datetime.datetime.now()
    idade = atual.year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('AO TODO TIVEMOS {} PESSOAS MAIORES DE IDADE!'.format(maior))
print('AO TODO TIVEMOS {} PESSOAS MENORES DE IDADE!'.format(menor))



