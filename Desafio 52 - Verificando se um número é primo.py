'''Crie um programa que leia um número inteiro e fale se ele é ou não um número primo!'''

num = int(input('Digite um número: '))
total = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(cont), end=' ')
print('\n\033[mO número {} foi dividido {} vezes '.format(num, total))
if total == 2:
    print('E por isso ele é PRIMO! ')
else:
    print('E po isso ele NÃO é primo! ')
