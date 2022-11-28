list = []
list_x = []
list_y = []
a = list.append(input('Digite algo: '))
for i, c in enumerate(list):
    if c == '2':
        list_x.append(c)
    elif c == '3':
        list_y.append(c)
print(list_y)
print(list_x)
