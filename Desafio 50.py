'''Crie um programa que leia seis números inteiros emostre a soma somente dos que forem pares, se for impar
desconsidere! '''
cont = 0
soma = 0
for pares in range(1,7):
    num = int(input('DIGITE UM NÚMERO:'))
    if num % 2 == 0:
         cont += 1
         soma += num
print('A SOMA DOS {} NÚMEROS PARES É {} !'.format(cont,soma))



