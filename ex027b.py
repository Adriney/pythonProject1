#Faça um programa que leia o nome completo de
# uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro=Ana
#Último= Souza
n = str(input("Digite seu nome completo: ")).strip().upper()
nome = n.split()  # .split() separar o nome em partes/lista
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format((nome[0])))
print("seu último nome é {}".format(nome[len(nome)-1]))