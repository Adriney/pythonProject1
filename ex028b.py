#Escreva um programa que faça o computador "pensar" em um
# número inteiro entre 0 e 4 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from  time import sleep
computador = randint(0,5)#faz computador escolher.
print("-=-" * 20)
print("Vou escolher um  número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

jogagor= int(input("Que número você escolhe? :"))
print("PROCESSANDO...")
sleep(3) # faz programa esperar
if jogagor == computador:
    print("Você conseguiu acertar!")
else:
    print("Número escolhido foi {}, e você digitou {}".format(computador, jogagor))