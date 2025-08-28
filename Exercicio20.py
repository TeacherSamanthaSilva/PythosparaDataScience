#Faça um algoritmo que armazenará os 5 números digitados pelo usuário em uma trupla. Ao final mostre os valores

lista = []
for i in range(5):
  n = int(input(f"Digite o valor {i+1}: "))
  lista.append(n)

t = tuple(lista)
print(lista)
print(t)