'''Crie um programa que leia dois números e mostre um menu na tela:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR NÚMERO
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA'''

opção = 0
pri = int(input('Primeiro número: '))
seg = int(input('Segundo número: '))
while opção != 5:
    print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
    opção = int(input('Digite sua opção!'))
    if opção == 1:
        soma = pri + seg
        print(f'A soma dos dois números é = {soma}!')
    elif opção == 2:
        multiplicação = pri * seg
        print(f'A multiplicação de  {pri} x {seg} é = {multiplicação}!')
    elif opção == 3:
        m = [pri, seg]
        maior = max(m)
        print(f'O maior número digitado foi {maior}!')
    elif opção == 4:
        print('Vamos digitar novos números!')
        pri = int(input('Primeiro número: '))
        seg = int(input('Segundo número: '))
    elif opção == 5:
        pass
    else:
        print('Opção inválida!')
