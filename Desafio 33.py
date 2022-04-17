'''Faça um programa que leia três números e mostre na tela qual é o menor e qual é o maior!'''

x = int(input('Digite um número!'))
xx = int(input('Digite o segundo número!'))
xxx = int(input('Digite o terceiro número!'))
xi = [x,xx,xxx]
m = max(xi)
mn = min(xi)
print('O maior número digitado foi {}!'.format(m))
print('O menor número digitado foi {}!'.format(mn))

