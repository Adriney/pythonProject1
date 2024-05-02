#Crie um programa que mostre na tela todos os números
# pares que estão no intervalo entre 1 e 50.
print('='*25)
print('\033[34m Números pares de 1 a 50.\033[m')
print('='*25)
def num_par (numero):
    pares = []
    for i in range(2, numero +1, 2):
       pares.append(i)
    return pares
resultado = num_par(50)
#print('Os números \033[31m pares \033[m de 50 são :\n',resultado)
print(resultado)