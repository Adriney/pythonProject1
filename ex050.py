#Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.
num1 = int(input('Digite o 1° número:'))
num2 = int(input('Digite o 2° número:'))
num3 = int(input('Digite o 3° número:'))
num4 = int(input('Digite o 4° número:'))
num5 = int(input('Digite o 5° número:'))
num6 = int(input('Digite o 6° número:'))

soma_pares = 0

if num1 % 2 == 0:
    soma_pares += num1
if num2 % 2 == 0:
    soma_pares += num2
if num3 % 2 == 0:
    soma_pares += num3
if num4 % 2 == 0:
    soma_pares += num4
if num5 % 2 == 0:
    soma_pares += num5
if num6 % 2 == 0:
    soma_pares += num6
print(f'A soma dos números pares é: {soma_pares}')
