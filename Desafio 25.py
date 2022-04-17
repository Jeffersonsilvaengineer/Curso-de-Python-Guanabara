'''Crie um progama que leia o nome de uma pessoa e mostre se tem o nome silva!'''

x = input('Digite seu nome completo!')
if "silva" in x:
    print('O nome {} , tem o sobre nome silva!'.format(x))
else:
    print('O nome: digitado não tem o sobre nome silva!')
