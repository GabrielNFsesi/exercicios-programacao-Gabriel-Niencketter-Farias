#GABRIEL_ESTRUTURA_DECISAO_5.py
nota1 = float(input("Digite sua primeira nota!"))
nota2 = float(input("Digite sua segunda nota!"))
media = (nota1 + nota2) / 2
if media==(10):
    print("Aprovado com Distinção")
elif media>=(7):
    print("Aprovado")
else: 
    print("Reprovado")