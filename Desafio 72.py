from num2words import num2words
numero = int(input('Digite um numero! '))
num_ptbr = num2words(numero, lang='pt-br')
print(f'você digiou o número {numero} ')
