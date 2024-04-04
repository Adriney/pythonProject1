#Faça um algorito que leia o salário e mostre seu, com 15% de aumento.
s = int(input("Qual é valor do seu salario:"))
aumt = 0.15
ns = s *(1 + aumt)
print("O valor no novo salario (com reajuste de 15%) será {} ".format(ns))