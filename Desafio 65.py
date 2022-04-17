'''Crie um programa que leia varios números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar se o usuário
quer ou não continuar a digitar valores!'''

cont = soma = media = menor = maior = 0
list = []
continuar = 'S'
while continuar in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    list += [n]
    continuar = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
media = soma / cont
print('FIM! você digitou {} números e a média desses valores é {}'.format(cont,media))
print('O maior valor é {} e o menor valor é {}'.format(max(list), min(list)))

