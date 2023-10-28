'''Crie um programa que leia varios números pelo teclado, o programa só deve parar quando o usuário
digitar o valor de 999, que é a condição de parada. No final mostre quantos números foram digitados
e qual a soma entre eles, (desconsiderando o flag).'''

cont = soma = numero = 0
numero = int(input('Digite um número: 999 PARA PARAR! '))

while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite um número: 999 PARA PARAR! '))
print(f'FIM!, VOCÊ DIGITOU {cont} NÚMEROS E A SOMA ENTRE ELES É {soma} !')
