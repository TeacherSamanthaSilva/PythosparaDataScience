# Procurando um item em uma lista
numeros = [4, 8, 15, 16, 23, 42]
item_a_procurar = 18

for numero in numeros:
    if numero == item_a_procurar:
        print(f"Item {item_a_procurar} encontrado!")
        break
else:
    print(f"Item {item_a_procurar} não encontrado.")