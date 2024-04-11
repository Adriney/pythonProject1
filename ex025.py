#Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.
nome =input("Qual o seu nome:")
nome = nome.upper()
#.upper() é usado para converter uma string em maiúsculas
#.lower() é usado para converter uma string em minúsculas
print("SILVA" in nome) # in é um operador do python e não um metodo
if "SILVA" in nome:
    print("Possui Silva no nome")
else:
    print("Não possui Silva no nome")
