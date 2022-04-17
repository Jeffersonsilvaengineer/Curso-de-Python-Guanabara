'''Faça um programa que leia pelo teclado o nome completo de uma pessoa,e mostre na tela o primeiro e o último nome
dessa pessoa! '''

nome = input('Digite seu nome completo!')
x = nome.split()
print('O nome digitado foi-->',nome)
print('Primeiro nome:',x[0])
print('Último nome:',x[-1])
