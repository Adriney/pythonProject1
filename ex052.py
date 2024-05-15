#Faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.
num = int(input('Digite um número:' ))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        #se número for divisivel por c(contador) ==(igual) a 0 imprima na cor...
        tot += 1 # se for divisivel tot recebe mais 1(tot = tot + 1)
        print('\033[36m',end='')
    else:# se não for divisivel imprima na cor ...
        print('\033[31m',end='')
    print(f'{c}',end='')
print(f'\n\033[m O número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('  E por isso ele É PRIMO!')
else:
    print('  E por isso ele NÃO É PRIMO!')
