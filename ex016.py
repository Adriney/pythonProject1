# Crie um progrmama que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção inteira.
#EX:Digite um número:6.127 O número tem a parte inteira 6.

real = float(input("Digite um número:"))

print("O número {} tem a parte Inteira {:.0f}".format(real, real))