#Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0, com uma pausa
# de 1 segundo entre eles.
import time
print('-='*15)
print('CONTAGEM REGRESSIVA')
print('-='*15)
segundos = 10
def cont_reg (segundos):
    while segundos >=0:
        print(segundos)
        time.sleep(1)
        segundos -=1

    print('Fim da contagem!!!')
cont_reg(10)

