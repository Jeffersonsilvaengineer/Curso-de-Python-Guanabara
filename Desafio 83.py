'''Crie um programa onde o usuário digite um expressão qualquer que use parênteses. Seu programa deverá analisar
se a expressão passada está comparêntese abertos e fechados na ordem correta'''
list = []
list_x = []
list_y = []
expr = str(input('Digite uma expressão: '))
for simb in expr:
    if simb == '(':
        list_x.append('(')
    elif simb == ')':
        list_y.append(')')
print('=-='*12)
print(f'A expressão digitada foi {expr}')
print('=-='*12)
if len(list_x) == len(list_y):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')


