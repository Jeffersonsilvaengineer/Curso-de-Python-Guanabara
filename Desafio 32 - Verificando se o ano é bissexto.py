'''Crie um progama que leia um ano qualquer e mostre na tela se ele é bissexto!
Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias,
um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos
(exceto anos múltiplos de 100 que não são múltiplos de 400). Isto é feito com o objetivo de manter o calendário anual
 ajustado com a translação da Terra e com os eventos sazonais relacionados às estações do ano. '''

ano = int(input('Digite um ano qualquer!'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
print('O ano {} não é bissexto!'.format(ano))
