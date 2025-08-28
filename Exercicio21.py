#Faça um algoritmo que carregue um dicionário de 5 elementos onde a chave é o sobrenome da pessoa e o valor a sua idade. Após a finalização da entrada, o algoritmo deve escrever o sobrenome da pessoa com maior idade.

# versão 1
d = {}
for i in range(5):
  nome = input(f"Digite o nome {i+1}: ")
  idade = int(input(f"Digite a idade {i+1}: "))
  d[nome] = idade
maior = 0
nome_maior = ''
for k, v in d.items():
  if v > maior:
    maior = v
    nome_maior = k

print(f"A pessoa com maior idade é {nome_maior} com {maior} anos!")