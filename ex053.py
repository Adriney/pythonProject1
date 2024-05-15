#Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromeo, desconsiderando os espaços.
# EX:APOS A SOPA / A SACADA DA CASA /A TORRE DA DERROTA /
# O LOBO AMA BOLO / ANOTARAM A DATA DA MATATONA
frase =  str(input('Digite uma frase: ')).strip().upper()
#.strip() ->tira o espaço entes e depois /.upper() -> deixa tudo maiúculo
palavras = frase.split() #separa nao vetor/lista
junto = ''.join(palavras)# deixa tudo em uma string
'''inverso = '''''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):#inverter a palavra/frase
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:# testar ve se inverso é igual a junto
    print('Temos um palíndromo!')#imprime tela se frase foi igual invertida
else:
    print('A frase digitada não é um palíndromo!')