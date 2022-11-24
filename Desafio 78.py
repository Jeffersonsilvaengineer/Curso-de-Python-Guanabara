'''Faça um programa que leia 5 valores numericos pelo teclado e guarde em uma lista, no final mostre: qual
foi o maior e o menor valor digitado e suas respectivas posições na lista'''

valores = list()
for x in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(f'O maior valor foi {max(valores)}, ele aparece na posição {valores.index(max(valores))+1}!')
print(f'O menor valor digitado foi {min(valores)}, ele aparece na posição {valores.index(min(valores))+1}!')
