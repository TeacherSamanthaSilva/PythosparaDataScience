#Escreva um programa que calcule quantos degraus uma pessoa precisa subir para alcançar uma certa altura.

altura_degrau = float(input("Digite a altura do degrau em cm: "))
altura_desejada = float(input("Digite a altura desejada em metros: "))
num_degraus = (altura_desejada * 100) / altura_degrau
print(f"Você precisa subir {num_degraus} degraus")