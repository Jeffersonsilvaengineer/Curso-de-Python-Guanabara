'''Crie um programa onde o usuário possa digitar vários valores númericos e cadastre em uma lista. Caso
o número exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos em ordem crescente'''

list = []
while True:
    v = int(input('Digite um número...'))
    if v in list:
        print('Valor duplicado! digite outro número...')
        continue
    list.append(v)
    print('Valor adicionado com sucesso...')
    cont = str(input('Quer continuar? [S/N] ')).upper()
    while cont not in 'S/N':
        cont = str(input('Resposta inválida! quer continuar? [S/N] ')).upper()
    if cont == 'N':
        break
print(list)


list = []
while True:
    v = int(input('Digite um número...'))
    if v in list:
        print('Valor duplicado! digite outro número...')
    else:
        list.append(v)
        print('Valor adicionado com sucesso...')
        cont = str(input('Quer continuar? [S/N] ')).upper()
        while cont not in 'S/N':
            cont = str(input('Resposta inválida! quer continuar? [S/N] ')).upper()
        if cont == 'N':
            break
print(list)
