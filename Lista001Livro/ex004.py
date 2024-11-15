# Lista de bolsas de valores
Bolsas = ['dow', 'ibov', 'ftse', 'dax', 'nasdaq', 'cac']

# (a) Selecionar as três primeiras bolsas
print("a) Três primeiras bolsas:", Bolsas[:3])

# (b) Incluir a sublista Bs = ['hong kong', 'merval'] na lista anterior
Bs = ['hong kong', 'merval']
Bolsas.extend(Bs)
print("b) Lista com sublista incluída:", Bolsas)

# (c) Descobrir qual o índice da 'nasdaq'
print("c) Índice da 'nasdaq':", Bolsas.index('nasdaq'))

# (d) Remover 'cac' da lista
Bolsas.remove('cac')
print("d) Lista após remover 'cac':", Bolsas)

# (e) Inserir "sp&500" como índice 2 na lista de bolsas
Bolsas.insert(2, "sp&500")
print("e) Lista após inserir 'sp&500' no índice 2:", Bolsas)
