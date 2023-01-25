'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
 em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! DIGITE APENAS [M/F] ')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    galera.append(pessoas.copy())
    while True:
        continuar = input('Quer continuar? [S/N]: ').upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! DIGITE APENAS [S/N] ')
    if continuar == 'N':
        break
print('=-' * 20)
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas!')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram --> ', end=' ')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=', ')
print()
print('D) Alista de pessoas que estão acima da média de idade é:', end=' ')
for p in galera:
    if p['Idade'] > media:
        print(f'{p["Nome"]}', end=', ')
print()
