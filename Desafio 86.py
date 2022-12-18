'''Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No
final mostre na tela formatação correta'''
#minha solução
matriz = [[], [], [], [], [], [], [], [], []]
cont = 3
cont2 = 6
for c in range(3):
    x = matriz[c].append(input(f'Digite um valor para [0, {c}]: '))
for c in range(3):
    x = matriz[cont + c].append(input(f'Digite um valor para [1, {c}]: '))
for c in range(3):
    x = matriz[cont2 + c].append(input(f'Digite um valor para [2, {c}]: '))
print(f'{matriz[0]}{matriz[1]}{matriz[2]}')
print(f'{matriz[3]}{matriz[4]}{matriz[5]}')
print(f'{matriz[6]}{matriz[7]}{matriz[8]}')

#solução do professor
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'DIGITE UM VALOR PARA {[l, c]}: '))
for c in range(3):
    for l in range(3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()




