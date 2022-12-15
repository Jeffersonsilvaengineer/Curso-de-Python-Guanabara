import random
from time import sleep
jogos = int(input('Quantos jogos você deseja? '))
valor = 0
for c in range(jogos):
    list_mega = []
    while True:
        numeros = random.randint(1, 60)
        if numeros in list_mega:
            continue
        else:
            list_mega.append(numeros)
        list_mega.sort()
        if len(list_mega) == 20:
                break
    sleep(0.1)
    print('=-=' * 18)
    print(f'Os números do {c+1}º jogo são --> {list_mega}')
print('=-='*18)
if len(list_mega) == 6:
    valor = 4.5 * jogos
elif len(list_mega) == 7:
    valor = 31.5 * jogos
elif len(list_mega) == 8:
    valor = 126 * jogos
elif len(list_mega) == 9:
    valor = 378 * jogos
elif len(list_mega) == 10:
    valor = 945 * jogos
elif len(list_mega) == 11:
    valor = 2079 * jogos
elif len(list_mega) == 12:
    valor = 4158 * jogos
elif len(list_mega) == 13:
    valor = 7722 * jogos
elif len(list_mega) == 14:
    valor = 13513.50 * jogos
elif len(list_mega) == 15:
    valor = 22522.50 * jogos
elif len(list_mega) == 16:
    valor = 36036 * jogos
elif len(list_mega) == 17:
    valor = 55692 * jogos
elif len(list_mega) == 18:
    valor = 83538 * jogos
elif len(list_mega) == 19:
    valor = 122094 * jogos
elif len(list_mega) == 20:
    valor = 174420 * jogos
print(f'O VALOR TOTAL DESTE BOLÃO É R$ {valor :0,} REAIS')
