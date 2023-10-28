'''Faça um programa que leia um número interiro e mostre sua fatorial'''

from time import sleep

numero = int(input('Digite um número: '))
fatorial = 1
c = numero
while c > 0:
    sleep(0.3)
    print(f' {c} ', end='')
    print('x' if c > 1 else ' = '' {} '.format(fatorial), end=''.format(c, ))
    fatorial *= c
    c -= 1
