#De acordo com a idade digitada diga se é criança, adolescente ou adulto

idade  = int(input("Digite a sua idade "))

if idade < 13:
    print("Criança")
elif idade >= 13 and idade < 18:
    print("Adolescente")
else:
    print("Adulto")