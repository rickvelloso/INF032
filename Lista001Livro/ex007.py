import statistics

# Lista de dados
lista = [2, 2, 3, 3, 3, -1, -1, -2, 0, 0, 0, 2, 4, 5, 1, 2, 2, 0, 0, 0, 2, 1, 5, 5, 7, 6, 5, 0, 0]

# (a) Soma de todos os elementos
soma = sum(lista)
print("a) Soma de todos os elementos:", soma)

# (b) Máximo elemento da lista
maximo = max(lista)
print("b) Máximo elemento da lista:", maximo)

# (c) Mínimo elemento da lista
minimo = min(lista)
print("c) Mínimo elemento da lista:", minimo)

# (d) Média dos elementos da lista
media = statistics.mean(lista)
print("d) Média dos elementos da lista:", media)

# (e) Mediana dos elementos da lista
mediana = statistics.median(lista)
print("e) Mediana dos elementos da lista:", mediana)

# (f) Moda dos elementos da lista
moda = statistics.mode(lista)
print("f) Moda dos elementos da lista:", moda)

# (g) Desvio-padrão amostral
desvio_padrao_amostral = statistics.stdev(lista)
print("g) Desvio-padrão amostral:", desvio_padrao_amostral)

# (h) Desvio-padrão populacional
desvio_padrao_populacional = statistics.pstdev(lista)
print("h) Desvio-padrão populacional:", desvio_padrao_populacional)

# (i) Contar o número de vezes que aparece o número 0
contagem_zero = lista.count(0)
print("i) Número de vezes que aparece 0:", contagem_zero)

# (j) Contar o número de vezes que aparece o número 5
contagem_cinco = lista.count(5)
print("j) Número de vezes que aparece 5:", contagem_cinco)

# (k) Ordenar a lista em ordem crescente
lista_crescente = sorted(lista)
print("k) Lista em ordem crescente:", lista_crescente)

# (l) Ordenar a lista em ordem decrescente
lista_decrescente = sorted(lista, reverse=True)
print("l) Lista em ordem decrescente:", lista_decrescente)
