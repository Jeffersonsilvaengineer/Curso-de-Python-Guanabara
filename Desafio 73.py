'''Crie uma tupla com os 20 times do campeonato brasileiro na ordem de colocação
depois mostre:
A, apenas os 5 primeiros colocados
B, apenas os 4 ultimos
C, uma lista com os times em ordem alfabética
D, em que posição está o time do santos.'''
tabela = ('PALMEIRAS', 'INTERNACIONAL','FLAMENGO', 'FLUMINENSE','CORINTHIANS', 'ATHLETICO-PR',
          'ATLETICO-MG', 'AMÉRICA-MG', 'GOIAS', 'SANTOS', 'BRAGANTINO', 'BOTAFOGO', 'SÃO PAULO',
          'CEARA', 'FORTALEZA', 'CORITIBA', 'CUIABA', 'AVAI', 'ATLETICO-GO', 'JUVENTUDE')
print('*='*20)
print('{:^40}'.format('TABELA DO BRASILEIRÃO 2022'))
print('*='*20)
print('5 Primeiros colocados =', tabela[:5])
print('*='*20)
print('4 últimos colocados =', tabela[-4:])
print('*='*20)
print('Classificação em ordem alfabética =\n', sorted(tabela))
print('*='*20)
print(f'O santos está na {tabela.index("SANTOS")+1}ª posição')
