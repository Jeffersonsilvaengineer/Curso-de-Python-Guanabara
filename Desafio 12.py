'''Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% desconto!'''

p = float(input('Qual o preço do produto?'))
d = p * 5/100
pd = p - d
print('O preço com 5% de desconto é {}!'.format(pd))
