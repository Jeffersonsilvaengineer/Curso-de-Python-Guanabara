''''crie um progama que leia um número e mostre sua porção inteira!'''

import math

# Primeira solução
n = float(input('Digite um número!'))
print('Voçê digitou o número {} e sua porção inteira é {}'.format(n,math.trunc(n)))

# Segunda solução
n = float(input('digite um numero!'))
print('Você digitou o número {} e sua parte inteira é {}!'.format(n,int(n)))

# Terceira solução
n = float(input('digite um numero!'))
print(f'Você digitou o número {n} e sua parte inteira é {int(n)}!')
