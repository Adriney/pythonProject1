#Escreva um programa que leia um número inteiro
# qualquer e peça para o usuário escolher qual
# será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

num = int(input("\033[34mDigite um número\033[m: "))
conv =int(input("\n\033[34mQual será a base de conversão\033[m:"
                "\n (1) para binário \n (2) para octal"
                "\n (3) para hexadecimal  \n\033[31mSua escolha é\033[m :"))
if conv == 1:
    binario = bin (num)
    print("Você digitou o número \033[31m{}\033[m e seu número  binário é :\033[31m{}\033[m".format(num,binario))
elif conv == 2:
    octal = oct(num)
    print("Você digitou o número {} e seu número octal é :\033[31m{}\033[m".format(num,octal))
elif conv == 3:
    hexadecimal = hex(num)
    print("Você digitou o número {} e seu número hexadecimal é :\033[31m{}\033[m".format(num,hexadecimal))
else:
    print("\033[34mNão foi possivel efetuar a conversão!\033[m")

