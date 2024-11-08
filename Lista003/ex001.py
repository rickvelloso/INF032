lista = [1, 5, 3, 20, 2]
print("Lista inicial:", lista)

print("Primeiro elemento", lista[0])
print("Ultimo elemento", lista[-1])
print("Elemento do meio", lista[len(lista) // 2])

lista[1] = 31
print("Lista modificada:", lista)

novo_elemento = int(input("Digite um elemento: "))
lista.append(novo_elemento)
print("Lista apos adicionar novo elemento: ", lista)

posicao_removida = int(input("Insira a posição da lista[0 a %d] que você deseja remover: " % (len(lista) - 1)))
lista.pop(posicao_removida)
print("Lista depois de remover o elemento na posição %d", posicao_removida)

print("Tamanho da lista: ", len(lista))

soma = sum(lista)
print("Soma dos elementos: ", soma)

lista_desordenada = [12, 7, 3, 18, 5]
lista_ordenada = sorted(lista_desordenada)
print("Lista ordenada:", lista_ordenada)

lista_invertida = lista[::-1]
print("Lista invertida:", lista_invertida)

numero_a_contar = 3
contagem = lista.count(numero_a_contar)
print(f"O número {numero_a_contar} aparece {contagem} vezes na lista.")

lista_com_cinco = [1, 2, 3, 4, 5]
fatia = lista_com_cinco[1:4]  
print("Fatia da lista:", fatia)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_mesclada = lista1 + lista2
print("Lista mesclada:", lista_mesclada)

numero_para_verificar = int(input("Digite um número para verificar se está na lista: "))
print(numero_para_verificar in lista)
    
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
lista_sem_duplicatas = list(set(lista_com_duplicatas))
print("Lista sem duplicatas:", lista_sem_duplicatas)



