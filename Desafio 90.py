''' Faça um programa que leia nome e média de um aluno guardando também sua situação em um dicionário
No final mostre o conteúdo da estrutura na tela. '''

aluno = dict()
aluno['Nome'] = str(input('NOME: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Recuperação'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
