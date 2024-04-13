#Escreva um programa que faça o computador "pensar" em um
# número inteiro entre 0 e 4 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
palp = int(input("Qual seu palpite: "))

from random import choice

num = [0, 1, 2, 3, 4]
sis = choice(num)
print("O número escolhido foi {}".format(sis))
if palp == sis:
    print("Parabéns! Você acertou seu palpite!")
else:
    print("Você errou seu palpite!")

