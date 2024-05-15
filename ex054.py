#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
menor = 0
maior = 0
for c in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {c}ª a pessoa nasceu? '))
    idade = 2024 - ano_nasc
    if idade < 18 :
        menor += 1
    else:
        maior +=1
print(f'{menor} Pessoas ainda não atingiram a maioridade!')
print(f'{maior} Pessoas já maiores de idade!')
