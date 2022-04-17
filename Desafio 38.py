'''Faça um progama que leia dois números inteiros e compareos mostrando na tela as seguintes informações: o primeiro
número é maior, o segundo número é maior, não existe número maior os dois são iguais'''

p = int(input('Digite o primeiro número!'))
s = int(input('Digite o segundo número!'))
if p > s:
    print('O primeiro número é maior!')
elif s > p:
    print('O segundo número é maior!')
else:
    print('Não tem número maior as dois números são iguais')
