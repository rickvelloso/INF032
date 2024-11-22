agenda = {}

cpf1 = input("Digite o CPF (1): ")
nome1 = input("Digite o nome (1): ")
idade1 = int(input("Digite a idade (1): "))
telefone1 = input("Digite o telefone (1): ")
agenda[cpf1] = {"nome": nome1, "idade": idade1, "telefone": telefone1}

cpf2 = input("Digite o CPF (2): ")
nome2 = input("Digite o nome (2): ")
idade2 = int(input("Digite a idade (2): "))
telefone2 = input("Digite o telefone (2): ")
agenda[cpf2] = {"nome": nome2, "idade": idade2, "telefone": telefone2}

cpf3 = input("Digite o CPF (3): ")
nome3 = input("Digite o nome (3): ")
idade3 = int(input("Digite a idade (3): "))
telefone3 = input("Digite o telefone (3): ")
agenda[cpf3] = {"nome": nome3, "idade": idade3, "telefone": telefone3}

cpf4 = input("Digite o CPF (4): ")
nome4 = input("Digite o nome (4): ")
idade4 = int(input("Digite a idade (4): "))
telefone4 = input("Digite o telefone (4): ")
agenda[cpf4] = {"nome": nome4, "idade": idade4, "telefone": telefone4}

cpf5 = input("Digite o CPF (5): ")
nome5 = input("Digite o nome (5): ")
idade5 = int(input("Digite a idade (5): "))
telefone5 = input("Digite o telefone (5): ")
agenda[cpf5] = {"nome": nome5, "idade": idade5, "telefone": telefone5}

print(f"{cpf1}: {agenda[cpf1]['nome']}-{agenda[cpf1]['idade']}-{agenda[cpf1]['telefone']}")
print(f"{cpf2}: {agenda[cpf2]['nome']}-{agenda[cpf2]['idade']}-{agenda[cpf2]['telefone']}")
print(f"{cpf3}: {agenda[cpf3]['nome']}-{agenda[cpf3]['idade']}-{agenda[cpf3]['telefone']}")
print(f"{cpf4}: {agenda[cpf4]['nome']}-{agenda[cpf4]['idade']}-{agenda[cpf4]['telefone']}")
print(f"{cpf5}: {agenda[cpf5]['nome']}-{agenda[cpf5]['idade']}-{agenda[cpf5]['telefone']}")