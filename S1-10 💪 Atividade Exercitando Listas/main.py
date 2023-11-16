list_1 = list(range(0, 31))
print("lista completa")
print(list_1)
print("último índice da lista")
print(list_1[-1])
print("alterando o segundo item da lista para kenzie")
list_1[2] = "kenzie"
print(list_1)
print("fatiando a lista")
lista_fatiada = list_1[1:4]
print(lista_fatiada)
print("alterando o valor ao final de lista_1")
list_1[-1] = 'Academy'
print(list_1)
print("Removendo os items referentes aos valores 'Kenzie' e 'Academy' ")
list_1.pop(2)
list_1.pop(-1)
print(list_1)

list_2 = sorted(list_1, reverse=True)
print("lista 1")
print(list_1)
print("lista 2, (ordem decrescente)")
print(list_2)

print("tamanho da lista 1")
print(len(list_1))

print("tamanho da lista 2")
print(len(list_2))

list_1.pop(-1)
list_2.pop(-1)

print("lista 1 sem o último item")
print(list_1)
print("lista 2, (ordem decrescente) sem o último item")

print("limpando as duas listas")
list_1 = []
list_2 = []
print(list_1)
print(list_2)

