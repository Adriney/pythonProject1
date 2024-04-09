#Crie um programa que leia o nome completo de uma pessoa e mostre:
# =>O nome com todas as letras maiúsculas.
# => O nome com todas as letras minúsculas.
# =>Quantas letras ao todo(sem considerar e espaços).
# =>Quantas letras tem o primeiro nome.


frase = input("Qual o seu nome:")
print(frase.upper())
print(frase.lower())
print(len(frase.replace(" ", "")))
frase = (frase.split()[0])
print(len(frase))

