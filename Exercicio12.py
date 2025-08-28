"""  Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes; """

# solicita os valores de cada um dos lados
a = float(input("Digite o valor do lado 'a': "))
b = float(input("Digite o valor do lado 'b': "))
c = float(input("Digite o valor do lado 'c': "))

# verifica se os lados podem formar um triângulo
ehtriangulo = False
if (a+b > c) and (a+c > b) and (b+c > a):
    ehtriangulo = True

# se não formarem, exibir a mensagem adequada
if not ehtriangulo:
    print("Os lados não podem formar um triângulo!")
    
# se formarem um triângulo, verificar qual o tipo
if ehtriangulo:
    if (a == b == c):   # Equilátero
        print("É um triângulo Equilátero!")
    elif (a == b) or (b == c) or (a == c):  # Isósceles
        print("É um triângulo Isósceles!")
    else:   # Escaleno
        print("É um triângulo Escaleno!")