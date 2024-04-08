# Crie um progrmama que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção inteira.
#EX:Digite um número:6.127 O número tem a parte inteira 6.

from math import trunc
num = float(input("Digite um valor: "))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))