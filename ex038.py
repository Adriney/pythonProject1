#Escreva um programa que leia dois números inteiros
# e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1>n2:
    print("O \033[36mprimeiro\033[m  valor é \033[36mmaior\033[m! ")
if n1<n2:
    print("O \033[33msegundo\033[m valor é \033[33mmaior\033[m!")
if n1 == n2:
    print("Não existe valor maior, \033[31mos dois são iguais\033[m!")
