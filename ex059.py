#Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
while True:
    op = int(input('Qual o tipo de operação deseja fazer:'
                     '\n[1] somar '
                     '\n[2] multiplicar '
                     '\n[3] maior '
                     '\n[4] novos números '
                     '\n[5] sair do programa \n' ))


    if op == 1:
        num1 = int(input('Digite 1° número:'))
        num2 = int(input('Digite 2° número:'))
        soma = num1 + num2
        print(f'A soma dos dois números é {soma}')
    elif op == 2:
        num1 = int(input('Digite 1° número:'))
        num2 = int(input('Digite 2° número:'))
        multiplicar = num1 * num2
        print(f'A multipicação dos dois números é {multiplicar}')
    elif op == 3:
        num1 = int(input('Digite 1° número:'))
        num2 = int(input('Digite 2° número:'))
        maior = max(num1,num2)
        print(f'O número maior entre os dos dois números é {maior}')
    elif op == 4:
        continue
    elif op == 5:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
