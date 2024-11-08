frutas = ["maçã", "banana", "laranja"]
docinhos_festa = ["brigadeiro", "beijinho", "cajuzinho"]
ingredientes_feijoada = ["feijão preto", "carne seca", "linguiça"]

listona = [frutas, docinhos_festa, ingredientes_feijoada]

brigadeiro = listona[1][0]
print("Brigadeiro:", brigadeiro)

listona[1].append("mais brigadeiro")
print("Lista de docinhos após adicionar mais brigadeiro:", listona[1])

listona.append("bebidas")
print("Listona após adicionar 'bebidas':", listona)


#ex004
del listona[:]
print("Listona após remoção de todos os elementos:", listona)