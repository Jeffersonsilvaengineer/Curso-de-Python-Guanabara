'''Crie um programa que leia vários números pelo teclado, o programa só deve parar quando o usuário
digitar o valor de 999, que é a condição de parada. No final mostre quantos números foram digitados
e qual a soma entre eles, (desconsiderando o flag).'''

cont = soma = n = 0
while True:
    n = int(input('Digite um número: 999 PARA PARAR! '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'FIM!, VOCÊ DIGITOU {cont} NÚMEROS E A SOMA ENTRE ELES É {soma} !')
