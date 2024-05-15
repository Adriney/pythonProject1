#Desenvolva um programa que leia o primeiro termo e a razão de uma
# PA(progressão aritmética). No final, mostre os 10 primeiros
# termos dessa progressão.
print('=='*12)
print('  10 TERMOS DE UMA PA  ')
print('=='*12)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
décimo = primeiro + (10 - 1) * razão
for c in  range(primeiro, décimo + razão, razão):
    print(f'{c}', end='-> ')
print('ACABOU')