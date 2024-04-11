#Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.
nome = str(input("qual é seu nome  completo? ")).strip()
print("Seu nome tem Silva? {}".format('silva' in nome.lower()))
#print("Seu nome tem Silva? {}".format('SILVA' in nome.upper()))


#.upper() é usado para converter uma string em maiúsculas
#.lower() é usado para converter uma string em minúsculas