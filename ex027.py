#Faça um programa que leia o nome completo de
# uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro=Ana
#Último= Souza
nome = input("Qual o seu nome:")
print(nome)
nome1 = nome.split()[0]

print("Primeira parte:", nome1)
nome2 = nome.split()[-1]
print("Última parte:", nome2)
