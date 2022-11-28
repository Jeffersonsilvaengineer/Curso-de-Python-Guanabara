'''Crie um programa que vai ler vários números e colocar em uma lista, depois disso crie duas lista extras que vão
 conter apenas os valores pares e o valores impares digitados respectivamente, ao final mostres as tres listas.'''

list_geral = []
list_par = []
list_impar = []
while True:
    x = list_geral.append(int(input('Digite um número: ')))
    cont = str(input('Quer continuar? [S/N] ')).upper()
    while cont not in 'S/N':
        cont = str(input('Resposta inválida! digite novamente [S/N]: ')).upper()
    if cont == 'N':
        break
for i, v in enumerate(list_geral):
    if v % 2 == 0:
        list_par.append(v)
    else:
        list_impar.append(v)
print(f'A lista completa é {list_geral}')
print(f'A lista de pares é {list_par}')
print(f'A lista de impares é {list_impar}')

