'''Crie um programa que vai gerar 5 números aleatórios e colocar dentro de uma tupla.
Depois disso, mostre a listagem de números gerados e tambem mostre o menor e o maior numero que estão na tupla.'''

from random import randint

lis = (randint(0,60), randint(0,60), randint(0,60), randint(0,60), randint(0,60))
love = lis
print(f'Os valores sorteados foram {lis} ')
print(f'O maior número sorteado foi {max(love)}')
print(f'O menor número sorteado foi {min(love)}')
