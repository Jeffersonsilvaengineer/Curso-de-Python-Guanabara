'''Escreva um progama para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
 o salário do comprador e em quantos anos ele vai pagar.
 Cálcule o valor da prestação mensal, sabendo que ela não pode exeder 30% de seu salário ou então seu emprestimo será negado.'''

vc = float(input('Qual o valor da casa desejada?'))
sa = float(input('Qual é seu salário?'))
qa = int(input('Em quantos anos você deseja pagar?'))
di = vc / (qa*12)
por = sa * 30/100
if di <= por:
    print('Parabéns seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo foi negado porque o valor da parcela ultrapassou 30% de seu salário!')
    