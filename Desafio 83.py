'''Crie um programa onde o usuário digite um expressão qualquer que use parênteses. Seu programa deverá analisar
se a expressão passada está comparêntese abertos e fechados na ordem correta'''
list = []
list_x = []
list_y = []
exp = list.append(input('Digite uma expressão: '))
for i, c in enumerate(list):
    if c == '(':
        list_x.insert(c)
    elif c == ')':
        list_y.insert(c)
print('=-='*12)
print(f'A expressão digitada foi {list}')
print('=-='*12)
if len(list_x) == len(list_y):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
print(list_y)
print(list_x)
