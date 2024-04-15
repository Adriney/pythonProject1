#Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.(r1,r2,r3)
r1 = int(input("Digite o comprimento da \033[32mprimeira\033[m reta:"))
r2 = int(input("Digite o comprimento da \033[34msegunda\033[m reta:"))
r3 = int(input("digite o comprimento da \033[36mterceira\033[m reta:"))
if (r1 + r2 > r3) and (r1 +r3 > r2) and (r2 +r3 > r1):
    print(" As medidas das retas {}, {}, {}, \033[31mpode\033[m formar um triângulo".format(r1,r2,r3))
else:
    print("As medidas das retas {}, {}, {}, \033[31mnão\033[m podem formar um triângulo".format(r1,r2,r3))