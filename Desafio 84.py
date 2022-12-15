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
    valor = 4.5 * 6
elif len(list_mega) == 7:
    valor = 31.5 * 7
elif len(list_mega) == 8:
    valor = 126 * 8
elif len(list_mega) == 9:
    valor = 378 * 9
elif len(list_mega) == 10:
    valor = 945 * 10
elif len(list_mega) == 11:
    valor = 2079 * 11
elif len(list_mega) == 12:
    valor = 4158 * 12
elif len(list_mega) == 13:
    valor = 7722 * 13
elif len(list_mega) == 14:
    valor = 13513.50 * 14
elif len(list_mega) == 15:
    valor = 22522.50 * 15
elif len(list_mega) == 16:
    valor = 36036 * 16
elif len(list_mega) == 17:
    valor = 55692 * 17
elif len(list_mega) == 18:
    valor = 83538 * 18
elif len(list_mega) == 19:
    valor = 122094 * 19
elif len(list_mega) == 20:
    valor = 174420 * 20
print(f'O VALOR TOTAL DESTE BOLÃO É R${valor} REAIS')
