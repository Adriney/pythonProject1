#Faça um programa que leia um número qualquer e mostre o seu factorial.
# Ex: 5!= 5x4x3x2x1=120

n = int(input('Digite um número para calcular seu fatorial:'))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c} ',end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c#f = f * c
    c -= 1
print(f'{c}')

