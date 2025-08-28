#Elabore um algoritmo para determinar quantas vogais existem dentro de uma determinada frase (que deve ser recebida do usuário).

frase = input("Digite uma frase: ")
qtd = 0
for letra in frase:
    if letra.upper() in 'AEIOU':
        qtd = qtd + 1
print(f"Na frase, existe(m) {qtd} vogais!")