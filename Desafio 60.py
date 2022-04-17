'''Faça um programa que leia um número interiro e mostre sua fatorial'''
from time import sleep
num = int(input('Digite um número: '))
fat = 1
c = num
while c > 0:
    sleep(0.5)
    print(' {} '.format(c),end='')
    print('x' if c > 1 else ' = '' {} '.format(fat),end=''.format(c,))
    fat *= c
    c -= 1
