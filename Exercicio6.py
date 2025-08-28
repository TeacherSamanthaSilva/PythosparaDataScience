#Escreva um programa que calcule a área de um círculo, dado o raio.

import math
raio = float(input("Digite o raio do círculo: "))
area = math.pi * (raio ** 2)
print(f"Área do círculo: {area}")