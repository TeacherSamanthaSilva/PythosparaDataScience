#Escreva um programa que leia o ano de nascimento e o ano atual, e calcule a idade em anos, meses, dias e semanas.

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_dias // 7
print(f"Idade: {idade_anos} anos, {idade_meses} meses, {idade_dias} dias, {idade_semanas} semanas")