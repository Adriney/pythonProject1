#Faça um programa que leia o nome completo de
# uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro=Ana
#Último= Souza
nome = input("Qual o seu nome:").upper()
print("Muito prazer em te conhecer {}!!!".format(nome))
nome1 = nome.split()[0]
print("Primeiro nome:", nome1)
nome2 = nome.split()[-1]
print("Último nome:", nome2)
