'''Faça um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final mostre: Qual o total da compra, quantos produtos custam
 mais de R$ 1000 reais, Qual o nome do produto mais barato.'''

total = mil = barato = valor = 0
print('='*23)
print('   LOJAS JEFFERSON!  ')
while True:
    print('='*23)
    produto = str(input('Nome do produto: '))
    valor = int(input('Qual o valor: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    total += valor
    if valor > 1000:
        mil += 1
    if continuar == 'N':
        break
print('='*9,'FIM','='*9)
print(f'O total da compra foi {total} reais!')
print(f'{mil} produtos custam mais de mil reais!')
print(f'O produto mais barato foi {barato}!')
