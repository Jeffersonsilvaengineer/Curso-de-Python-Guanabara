'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.'''
jogador = dict()
gols = list()
time = list()
soma = 0
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for c in range(jogador['Partidas']):
        gols.append(int(input(f'Quantos gols {jogador["Nome"]} fez na {c + 1}ºPartida: ')))
        jogador['Gols'] = gols
    for gol in gols:
        soma += gol
    jogador['Total DE GOLS'] = soma
    time.append(jogador.copy())
    while True:
        continuar = input('Quer continuar? [S/N]: ').upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! DIGITE APENAS [S/N] ')
    if continuar == 'N':
        break
print('=-' * 20)
print(f'{"Cod":<4} {"Nome":<15} {"Gols":<15} {"Total":<2}')
for i, a in enumerate(time):
    print(f'{i + 1:<4}{jogador["Nome"]:<15}{jogador["Gols"]:>8.1f}')
while True:
    print('=-' * 10)
    opc = int(input('Notas de qual aluno? [99 -->PAR9AR] '))
    if opc == 999:
        break
