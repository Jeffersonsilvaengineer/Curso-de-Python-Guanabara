'''Faça um programa que leia o peso de cinco pessoas e mostre qual é o maior e qual é o menor!'''

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa!'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso digitado foi {} !'.format(maior))
print('O menor peso digitado foi {} !'.format(menor))
