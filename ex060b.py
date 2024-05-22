#Faça um programa que leia um número qualquer e mostre o seu factorial.
# Ex: 5!= 5x4x3x2x1=120

from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(F'O fatorial de {n} é {f}.')