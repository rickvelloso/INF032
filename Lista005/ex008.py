nome = input("Digite o nome do aluno:")
nota1 = float(input("Digite a primeira nota:" ))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2 ) / 2

if media >= 7:
    status = "Aprovado"
elif media < 3:
    status = "Reprovado"
else:
    status = "Em prova final"
    
print(f"Nome: {nome}, Nota 1: {nota1}, Nota 2: {nota2}, Média: {media:.2f}, Status: {status} ")