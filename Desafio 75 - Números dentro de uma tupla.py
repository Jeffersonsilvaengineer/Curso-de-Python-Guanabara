'''Desenvolva um programa que leia quatro valores pelo teclado e guardeos em uma tupla, no final mostre:

Quantas vezes aparece o valor 9!
Em que posição foi digitado pela primeira vez o valor 3!
Quais foram os números pares!'''

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o quarto número: ')))

print(f'Você digitou os valores: {num}')
if 9 in num:
       print(f'O número 9 foi digitado {num.count(9)} vezes!')
else:
       print('O número 9 não foi digitado!')
if 3 in num:
       print(f'O número 3 apareceu pela primeira vez na {num.index(3)+1}ª posição! ')
else:
       print('O número 3 não foi digitado')
print('Os números pares foram: ', end='')
for par in num:
       if par % 2 == 0:
              print(par, end=' ')


