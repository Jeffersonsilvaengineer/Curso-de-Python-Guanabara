qualidade = [
    {'nome': 'jefferson', 'idade': 31, 'sexo': 'masculino'},
    {'nome': 'simeia', 'idade': 36, 'sexo': 'feminino'},
    {'nome': 'luis', 'idade': 42, 'sexo': 'masculino'},
    {'nome': 'jefim', 'idade': 23, 'sexo': 'masculino'},
    {'nome': 'marcia', 'idade': 41, 'sexo': 'feminino'},
    {'nome': 'padrão', 'idade': 33, 'sexo': 'masculino'}
]

for pessoa in qualidade:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo: {pessoa['sexo']}")
