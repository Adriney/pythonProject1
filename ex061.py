#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''print('=='*12)
print('  10 TERMOS DE UMA PA  ')
print('=='*12)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
décimo = primeiro + (10 - 1) * razão
for c in  range(primeiro, décimo + razão, razão):
    print(f'{c}', end='-> ')
print('ACABOU')'''

print('=='*12)
print('  10 TERMOS DE UMA PA  ')
print('=='*12)

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
termo = primeiro
cont = 1  # Inicializa o contador em 1 para contar os termos

while cont <= 10:# Enquanto o contador for menor ou igual a 10
    print(f'{termo}', end=' -> ')
    termo += razão # Calcula o próximo termo da PA
    cont += 1 # Incrementa o contador

print('ACABOU')