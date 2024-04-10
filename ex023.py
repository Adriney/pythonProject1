#Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.
#Ex: digite um número: 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
numero = input("Digite um número:")
print("Analisando o número {}".format(numero))
print("unidade:",numero[3])
print("dezena:",numero[2])
print("centena:",numero[1])
print("milhar:",numero[0])