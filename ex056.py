#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

somaidade = 0
médiaidade = 0
mairidadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        mairidadehomen = idade
        nomevelho = nome
    if sexo in 'M' and idade > mairidadehomen:
        mairidadehomen = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade} anos')
print(f'O homen mais velho tem {mairidadehomen} anos, e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulhere(s) com menos de 20 anos.')