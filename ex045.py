#Crie um programa que faça o computador jogar
# Jokenpô com você(pedra/papel/tesoura).
from random import choice
n0 = str(input("Jokenpô!!! qual sua apósta:"))
n1 = "pedra"
n2 = "papel"
n3 = "tesoura"
lista = [n1,n2,n3]
pc = choice(lista)
print("\033[33m Você escolheu {}\033[m, e o \033[35m computador escolheu {}\033[m".format(n0,pc))
if  n0 == pc:
    print("Empate")
elif (n0 =="tesoura" and pc == "papel") or \
      (n0 =="papel" and pc == "pedra") or \
      (n0 =="pedra" and pc == "tesoura") :
    print("Você venceu!!!")
else:
    print("Você perdeu")