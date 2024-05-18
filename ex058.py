#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 a 10. Só que agora o jogador vai tentar
# advinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
from  random import  randint
from time import sleep
from random import randint
from  time import sleep
computador = randint(0,10)#faz computador escolher.
print("-=-" * 20)
print("Vou escolher um  número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)

palpites = 0

while True:
    palpite = int(input("Que número você escolhe? :"))
    #print(f' computador :{computador}.')
    palpites += 1
    if palpite == computador:
        print("Você conseguiu acertar!")
        break
else:
    print("Você errou! Tente novamente.")

print(f'O computador escolheu {computador} e você digitou {palpite}.'
      f'\n Foram necessários {palpites} palpites para conseguir acertar/vencer.')