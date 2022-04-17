'''Crie um programa que leia varios números pelo teclado, o programa só deve parar quando o usuário
digitar o valor de 999, que é a condição de parada. No final mostre quantos números foram digitados
e qual a soma entre eles, (desconsiderando o flag).'''

cont = 0
n = ''
while n != 999:
    cont += 1
    n = int(input('Digite um número: '))
    if n == 999:
        print('FIM!, VOCÊ DIGITOU O NÚMERO {} , DEPOIS DE {} TENTATIVAS!'.format(n,cont))


