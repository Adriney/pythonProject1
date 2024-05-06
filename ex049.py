#Refaça o desafio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número : '))
print("=====================")
for i in range(1, 11): # Loop de 1 a 10 para multiplicar o número pela contagem
    tab = num * i

    print("\033[36m {}\033[m x \033[34m {}\033[m = \033[31m {}\033[m".format(num, i, tab))
