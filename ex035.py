#Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.(r1,r2,r3)
r1 = float(input("Digite o comprimento da primeira reta:"))
r2 = float(input("Digite o comprimento da segunda reta:"))
r3 = float(input("digite o comprimento da terceira reta:"))
if (r1 + r2 > r3) and (r1 +r3 > r2) and (r2 +r3 > r1):
    print(" As medidas das retas {}, {}, {}, pode formar um triângulo".format(r1,r2,r3))
else:
    print("As medidas das retas {}, {}, {}, nao podem formar um triângulo".format(r1,r2,r3))