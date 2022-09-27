'''Crie um programa que vai gerar 5 números aleatórios e colocar dentro de uma tupla.
Depois disso, mostre a listagem de números gerados e tambem mostre o menor e o maior numero que estão na tupla.'''
from random import randint

lis = randint(0,100)
for c in range(lis):
    print(c)
print(f'Os valores sorteados foram {lis} ')
print(f'O maior número sorteado foi {lis}')
print(f'O menor número sorteado foi {lis}')
#
# for c in range(10, -1, -1):
#     sleep(1)
#     print(c)