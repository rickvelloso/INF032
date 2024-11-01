numero_conta = input("Digite o número da conta (três dígitos): ")

numero_inverso = numero_conta[::-1]
soma = int(numero_conta) + int(numero_inverso)
verificador = (int(str(soma)[0]) * 1) + (int(str(soma)[1]) * 2) + (int(str(soma)[2]) * 3)
digito_verificador = verificador % 10

print("Dígito verificador: {}".format(digito_verificador))
