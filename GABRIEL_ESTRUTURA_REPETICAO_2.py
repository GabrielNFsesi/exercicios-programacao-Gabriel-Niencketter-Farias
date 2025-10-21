#GABRIEL_ESTRUTURA_REPETICAO_2.py
nomeDeUsuario = input("Digite um nome de usuário! ")
senhaDeUsuario = input("Digite sua senha! ")
while nomeDeUsuario == senhaDeUsuario:
    print("Erro! A senha não pode coincidir com o nome de usuário!")
    nomeDeUsuario = input("Digite um nome de usuário! ")
    senhaDeUsuario = input("Digite sua senha! ")
print("Usuário e senha válidos!")