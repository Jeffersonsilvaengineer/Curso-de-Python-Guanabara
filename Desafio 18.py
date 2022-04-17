'''Faça um progama que leia um ângulo qualquer e mostre na tela seu seno, cosseno e tangente desse ângulo!'''

from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo!'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}!'.format(angulo,seno))
print('O ângulo de {} tem o cosseno de {:.2f}!'.format(angulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}!'.format(angulo, tangente))

