'''Crie um programa que leias varios nomes e pesos e gurde tudo em uma lita, no final mostre:
A)Quantas pessoas foram cadastradas!
B)Qual o pesso e nome da pessoa mais pesada!
C)Qual o nome e peso da pessoa mais leve!'''

list_temp = []
list_total = []
maior = menor = 0
while True:
    list_temp.append(str(input('NOME: ')))
    list_temp.append(float(input('PESO: ')))
    if len(list_total) == 0:
        maior = menor = list_temp[1]
    else:
        if list_temp[1] > maior:
            maior = list_temp[1]
        if list_temp[1] < menor:
            menor = list_temp[1]
    list_total.append(list_temp[:])
    list_temp.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('RESPOSTA INVÁLIDA! Quer continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
print(f'ESSAS FORAM TODAS AS PESSOAS CADASTRADAS --> {list_total}')
print(f'AO TODO FORAM CADASTRADAS {len(list_total)} PESSOAS!')
print(f'O MAIOR PESO FOI {maior}KG, E PERTENÇE A -->', end=' ')
for p in list_total:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O MENOR PESO FOI {menor}KG, E PERTENÇE A -->', end=' ')
for p in list_total:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()

