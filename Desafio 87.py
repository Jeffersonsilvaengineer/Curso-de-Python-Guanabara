'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = som3c = maior2l = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'DIGITE UM VALOR PARA {[l, c]}: '))
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^4}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('=-' * 20)
print(f'A soma de todos os valores pares digitados foi: {somapar}')
for l in range(0, 3):
    som3c += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {som3c}')
for c in range(0, 3):
    if c == 0:
        maior2l = matriz[1][c]
    elif matriz[1][c] > maior2l:
        maior2l = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior2l}')
