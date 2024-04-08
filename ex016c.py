# Crie um progrmama que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção inteira.
#EX:Digite um número:6.127 O número tem a parte inteira 6.

num = float(input("Digite um valor: "))
print("O valor digitado foi {} e sua porção inteira é {}".format(num, int(num)))