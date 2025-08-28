""" Faça um algoritmo que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a fórmula a seguir.

E = (2 ** 1) + (2 ** 2) + (2 ** 3) + ... + (2 ** N) """

n = int(input("Digite o valor n: "))
E = 0
for k in range(1, n+1):
    E = E + (2 ** k)

print(f"O valor de E = {E}")