#Faça um algoritmo que carregue um vetor de 5 elementos numéricos inteiros. Após a finalização da entrada, o algoritmo deve escrever o mesmo vetor, na ordem inversa de entrada.

lista = []
for i in range(5):
  n = int(input(f"Digite o valor {i+1}: "))
  lista.append(n)

print("Lista Inversa: ", lista[::-1])