'''Crie um programa onde o usuário possa digitar 5 valores numeréricos e cadastre em uma lista
já na posição correta de iserção sem usar o sort(), no final mostre a lista ordenada na tela.'''

list = []
for c in range(5):
    v = int(input(f'Digite o {c+1}ª número: '))
    if c == 0 or v > list[-1]:
        list.append(v)
        print('Valor adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(list):
            if v <= list[pos]:
                list.insert(pos, v)
                print(f'Valor adicionado na posiçao {pos}ª da lista!')
                break
            pos += 1
print(f'Os valores digitados em oredem crescente  foram: {list}')


