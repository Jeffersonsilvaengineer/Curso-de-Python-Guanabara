'''Calcule o preço a ser pago por um produto levando em consideração a forma de pagamento!
A VISTA NO DINHEIRO UO CHEQUE 10% DE DESCONTO!
A VISTA NO CARTÃO 5% DE DESCONTO!
EM ATÉ 2 VEZES NO CARTÃO PREÇO NORMAL!
3 VEZES OU MAIS NO CARTÃO 20% DE JUROS!'''

print('{:=^80}'.format('LOJAS JEFFERSON'))
pp = float(input('Qual o preço do produto? R$'))
print('Qual a forma de pagamento?')
fp = int(input('Digite 1 PARA A VISTA NO DINHEIRO UO CHEQUE!\nDigite 2 PARA A VISTA NO CARTÃO!\nDIGITE 3 PARA EM ATÉ 2 VEZES NO CARTÃO!\nDIGITE 4 PARA '
               '3 VEZES OU MAIS NO CARTÃO!'))
opc1 = pp - (pp * 10/100)
opc2 = pp - (pp * 5/100)
opc3 = pp
opc4 = pp + (pp * 20/100)
if fp == 1:
    print('O PREÇO DO PRODUTO É R$', opc1)
elif fp == 2:
    print('O PREÇO DO PRODUTO É R$', opc2)
elif fp == 3:
    print('O PREÇO DO PRODUTO É R$', opc3)
else:
    print('O PREÇO DO PRODUTO É R$', opc4)
