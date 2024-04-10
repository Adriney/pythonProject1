#Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.
nome =input("Qual o seu nome:")
nome = nome.upper()
print("SILVA" in nome)
if "SILVA" in nome:
    print("Possui Silva no nome")
else:
    print("Não possui Silva no nome")
