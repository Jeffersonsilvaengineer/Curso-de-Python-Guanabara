'''Crie um progama que mostre o salario de uma pessoa e calcule seu novo salário com 15% de aumento!'''

s = int(input('Digite seu salario!'))
au = s * 15/100
ns = s + au
print('Seu novo salário com 15% de aumento é {}!'.format(ns))
