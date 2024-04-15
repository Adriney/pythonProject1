#Crie um programa que leia um número inteiro e mostre
# na tela se ele é PAR ou IMPAR.

num = int(input("Digite um número:"))
if num % 2 == 0:
    print("O numero {} é \033[32mPAR\033[m!".format(num))
else:
    print("O número {} é \033[34mIMPAR\033[m!".format(num))