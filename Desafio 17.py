'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo'
      'e calcule  e mostre o comprimento da hipotenusa!'''

import math
co = int(input('Digite o comprimento do cateto oposto!'))
ca = int(input('Digite o comprimento do cateto adjacente!'))
coca = co**2 + ca**2
hip = math.sqrt(coca)
print('O comprimento do cateto oposto é {}!\no comprimento do cateto adjacente é {}!\n'
      'O comprimento da hipotenusa é {:.2f}!'.format(co, ca, hip))
