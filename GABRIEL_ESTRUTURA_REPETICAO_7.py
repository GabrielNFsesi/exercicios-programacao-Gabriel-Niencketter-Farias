#GABRIEL_ESTRUTURA_REPETICAO_7.py
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numero4 = float(input("Digite o quarto número: "))
numero5 = float(input("Digite o quinto número: "))

maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
if numero4 > maior:
    maior = numero4
if numero5 > maior:
    maior = numero5
print("O maior número é:", maior)