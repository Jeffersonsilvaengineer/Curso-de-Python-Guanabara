dados = list()
dados.append('jefferson')
dados.append(25)
pessoas = []
pessoas.append(dados[:])
pessoas.append('joão')
pessoas.append(32)
print(pessoas)
pessoas = [['jefferson', 29],['simeia', 34],['palmeiras', 105], ['titan', 2022]]
print(pessoas[2][0])
print(pessoas[0][1])
print(pessoas[2])
print(pessoas)
for c in pessoas:
    print(f'{c[0]} tem {c[1]} anos de idade!')
teste = list()
test2 = list()
maior = menor = 0
for c in range(3):
    test2.append(str(input('Digite um nome: ')))
    test2.append(int(input('Digite sua idade: ')))
    teste.append(test2[:])
    test2.clear()
for c in teste:
    if c[1] >= 18:
        maior +=1
        print(f'{c[0]} é maior de idade!')
    else:
        menor += 1
        print(f'{c[0]} é menor de idade!')
print(f'{maior} maior de idade e {menor} menores de idade!')