'''Crie um programa que leia nome e duas notas de alunos e gurade tudo dentro de uma lista composta. No final mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas individuais de cada aluno'''

list_alunos = []
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2) / 2
    list_alunos.append([nome, [nota1, nota2], media])
    cont = input('QUER CONTINUAR? [S/N]:').upper()
    while cont not in 'SN':
        cont = input('RESPOSTA INVÁLIDA! QUER CONTINUAR? [S/N]:').upper()
    if cont == 'S':
        continue
    elif cont == 'N':
        break
print('-=' * 20)
print(F'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('---' * 10)
for i, a in enumerate(list_alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=-' * 10)
    opc = int(input('Notas de qual aluno? [999 -->PARAR] '))
    if opc == 999:
        break
    elif opc <= len(list_alunos) - 1:
        print(f'Notas de {list_alunos[opc][0]} são {list_alunos[opc][1]}')
print('<<<< VOLTE SEMPRE >>>>')
