'''Crie um programa que leia vários valores e guarde em uma lista, depois disso mostre:
A: Quantos números foram digitados?
B: A lista de valores ordenados de forma decrescente!
C: Se o valor 5 foi digitado e está ou não na lista!'''

list = []
n = 0
while True:
    l = int(input('Digite um valor: '))
    n += 1
    list.append(l)
    list.sort()
    list.reverse()
    if '5' in list:
        x = list
    c = str(input('Quer continuar? [S/N] ')).upper()
    while c not in 'S/N':
        c = str(input('Resposta inválida! digite novamente: ')).upper()
    if c == 'N':
        break
print(f'Ao total foram digitados {n} numeros!')
print(f'Os valores digitados em ordem decrecente foram {list}')
if 5 in list: print('O numero 5 foi digitado e está presente na lista!')




