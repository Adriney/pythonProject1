#Faça um programa que leia um número qualquer e mostre o seu factorial.
# Ex: 5!= 5x4x3x2x1=120

num = int(input('Digite um número qualquer :'))
# Define o número para calcular o fatorial

def factorial(n):# Define uma função chamada factorial que recebe um argumento 'n'
    if n == 0: # Se 'n' for igual a 0
        return  1 # Retorna 1 (pois o fatorial de 0 é 1)
    else: # Caso contrário
        return n * factorial(n-1)  # Retorna o produto de 'n' e o fatorial de 'n-1'


res = factorial(num) # Chama a função factorial com 'numero' como
# argumento e armazena o resultado
print(f'O factoril de {num} é {res}') # Imprime o resultado