#GABRIEL_ESTRUTURA_REPETICAO_1.py
numero=11
while numero<0 or numero>10:
  numero = float(input("Digite um número entre 0 e 10!"))
  if numero <= 10 and numero >= 0:
    print("Você digitou o número",numero,"!")
  else:
    print("Valor inválido!")