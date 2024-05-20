#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

r = 'S'# Define a variável 'r' como 'S' para iniciar o loop
num = []# Lista para armazenar os números
while r == 'S':
    n = int(input('Digite um valor:'))
    num.append(n) # Adiciona o número à lista de números

    r = str(input('Quer continuar? [S/N]')).upper()

media = sum(num) / len(num)
maior = max(num)
menor = min(num)

print(f'A média dos valores foi {media:.2f}'
          f'\n O maior valor foi {maior}'
          f'\n O menor valor foi {menor}')

