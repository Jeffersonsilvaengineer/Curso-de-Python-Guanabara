'''Crie um progama que leia um número inteiro e mostre na tela se ele é par ou impar!'''

n = int(input('Digite um número!'))
d = (n % 2)
if d==0:
    print('O número é par!')
else:
    print('O número é impar!')
