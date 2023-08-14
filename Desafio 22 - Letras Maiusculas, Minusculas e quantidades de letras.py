'''Crie um progama que leia o nome completo de uma pessoa e mostre na tela o nome com todas as letra maiusculas
e com todas as letras minúsculas, mostre quantas letras tem ao todo sem contar os espaços, mostre  quantas letras
 tem o primeiro nome!'''

nome = input('Digite seu nome completo!')
print(nome.upper())
print(nome.lower())
p = nome.split()
print(len(''.join(p)))
print(len(p[0]))




