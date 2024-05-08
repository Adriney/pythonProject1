#Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
soma = 0  #recebe a soma de todos os números
cont = 0  #recebe a quantidade de números que foi somado
for c in range(1, 501, 2):
    if c % 3 == 0: #Números divisiveis por 3 igual a 0
        cont += 1 #Contabiliza a quantidade de números que foi somado
        soma += c #soma recebe o que ela tem mais o número.
      #print(c, end=' ') Aparece os números de divisiveis por 3
print(f'A soma de todos os {cont} valores solicitados é {soma}.')