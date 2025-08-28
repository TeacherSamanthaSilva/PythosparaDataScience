# Avaliando a nota do aluno com base no input
nota = float(input("Digite a sua nota: "))

if nota >= 90:
    print("Excelente!")
elif nota >= 75:
    print("Bom!")
elif nota >= 50:
    print("Satisfatório.")
else:
    print("Precisa melhorar.")