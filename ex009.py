#faça um programa que leia um número Interio qualquer
# e mostre na tela a sua tabuada.
num = int(input('Digite um número : '))
print("=====================")
for i in range(1, 11): # Loop de 1 a 10 para multiplicar o número pela contagem
    tab = num * i

    print("{} x {} = {}".format(num, i, tab ))


