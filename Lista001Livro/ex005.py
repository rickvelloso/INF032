# Abrir ou criar o arquivo 'bov.txt' e salvar os dados nele
with open("bov.txt", "w") as file:
    # Dados a serem salvos
    dados = ['petr4', 'vale3', 'ggbr4', 28.4, 31.3, 15.76]
    # Convertendo cada elemento em string e escrevendo no arquivo
    file.write(", ".join(map(str, dados)))

print("Dados salvos em 'bov.txt'")
