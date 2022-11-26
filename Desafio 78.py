'''Faça um programa que leia 5 valores numericos pelo teclado e guarde em uma lista, no final mostre: qual
foi o maior e o menor valor digitado e suas respectivas posições na lista'''

valores = []
for x in range(5):
    valores.append(int(input(f'Digite um valor na posição {x}: ')))

min_value = min(valores)
max_value = max(valores)

print(f'O maior valor foi {max_value}, ele aparece na posição {", ".join([str(i) for i, number in enumerate(valores) if number == max_value])}!')
print(f'O menor valor digitado foi {min_value}, ele aparece na posição {", ".join([str(i) for i, number in enumerate(valores) if number == min_value])}!')
