#Faça um programa que leia uma frase pelo teclado e mostee:
#>Quantas vezes aparece a letra "A".
#>Em que posição ela aparece a primeira vez.
#>Em que posição ela aparece a última vez.
frase = input("Digite sua frase:")
frase=frase.upper()
print(frase)
print("Possui {} letras 'A' na frase!".format(frase.count("A")))
print("primeira posição da letra 'A' é: {}".format(frase.find("A")+1))
# +1 para ajustar a indexação (Python começa a indexação a partir de 0).
print("Ultima  posição da letra 'A' é: {}".format(frase.rfind("A")+1))
