'''Crie um programa onde o usuário possa digitar 5 valores numeréricos e cadastre em uma lista
já na posição correta de iserção sem usar o sort(), no final mostre a lista ordenada na tela.'''

list = []
for c in range(5):
    v = int(input(f'Digite o {c+1}ª número: '))
    list.append(v)
print(list)


