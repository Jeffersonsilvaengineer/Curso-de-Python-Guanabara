''' Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
gols = list()
soma = 0
jogador['Nome'] = str(input('Nome: '))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
for c in range(jogador['Partidas']):
     gols.append(int(input(f'Quantos gols {jogador["Nome"]} marcou na {c + 1}ºPartida: ')))
     jogador['Gols'] = gols
for gol in gols:
     soma += gol
jogador['Total DE GOLS'] = soma
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
     print(f'O campo {k} tem valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for c in range(jogador["Partidas"]):
     print(f'=> Na partida {c + 1}, fez {jogador["Gols"][c]} gols.')
print(f'Foi um total de {soma} gols.')
