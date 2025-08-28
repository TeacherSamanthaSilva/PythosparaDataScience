#Faça um programa que receba um número inteiro x. Calcule e mostre o fatorial desse número (x!).

x = int(input("Digite o valor de x: "))
fatorial = 1
for i in range(1, x+1):
    fatorial = fatorial * i
print(f"O fatorial de {x} é {fatorial}")