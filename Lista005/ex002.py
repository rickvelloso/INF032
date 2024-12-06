nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
sexo = input("Digite o sexo (M/F) ").upper()

if sexo == "F" and idade < 25:
    print("ACEITA")
else: 
    print("NÃO ACEITA")