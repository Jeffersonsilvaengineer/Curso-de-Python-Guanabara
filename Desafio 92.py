'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
pessoa = dict()
while True:
    pessoa['Nome: '] = str(input('Nome: '))
    ano = int(input('Ano de nascimento: '))
    idade = datetime.now().year - ano
    pessoa['Idade: '] = idade
    pessoa['Ctps: '] = int(input('Carteira de trabalho [0 não tem!]: '))
    if pessoa['Ctps: '] == 0:
        break
    pessoa['Contratação: '] = int(input('Ano de contratação: '))
    y = (pessoa['Contratação: ']) - ano + 35
    pessoa['Aposentadoria: '] = y
    pessoa['Salário: '] = float(input('Salário: R$'))
    break
for k, v in pessoa.items():
    print(f'- {k:>15} tem o valor {v}')
