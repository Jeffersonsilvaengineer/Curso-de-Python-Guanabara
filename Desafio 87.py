'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'DIGITE UM VALOR PARA {[l, c]}: '))
for c in range(3):
    for l in range(3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()

somatotal = matriz[0][0]+matriz[0][1]+matriz[0][2]+matriz[1][0]+matriz[1][1]+matriz[1][2]+matriz[2][0]+matriz[2][1]+matriz[2][2]
som3 = matriz[2][0]+matriz[2][1]+matriz[2][2]
maior2l= (matriz[0][1], matriz[1][1], matriz[2][1])
maior2l = max(maior2l)
print(f'A soma de todos os valores pares digitados foi: {somatotal}')
print(f'A soma dos valores da terceira coluna é: {som3}')
print(f'O maior valor da segunda linha é: {maior2l}')
