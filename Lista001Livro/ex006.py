# Abrir o arquivo 'bov.txt' em modo de leitura e imprimir seu conteúdo
with open("bov.txt", "r") as file:
    conteudo = file.read()
    print("Conteúdo de 'bov.txt':", conteudo)
