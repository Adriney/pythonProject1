#Desenvolva uma lógica que leia o peso e a altura
# de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# - Abaixo de 18.5:Abaixo do peso
# - Entre 18.5 e 25:peso ideal
# - 25 até 30:Sobrepeso
# - 30 até 40:Obesidade
# - Acima de 40:Obesidade mórbida
print("-=-"*12)
print("CALCULE SEU IMC")
print("-=-"*12)
peso = float(input("Qual o seu \033[31mpeso\033[m:"))
altura = float(input("qual é a sua \033[31maltura\033[m:"))
imc = (peso / (altura * altura))

if  (imc < 18.5):
    print("Seu IMC é {}, você está abaixo do peso!".format(imc))
elif 18.5 < imc < 25 :
    print("Seu IMC é {}, você está no peso ideal!".format(imc))
elif 25 < imc < 30 :
    print("Seu IMC é {}, você está com Sobrepeso!".format(imc))
elif 30 < imc < 40:
    print("Seu IMC é {}, você está com Obesidade!".format(imc))
else:
    #(imc > 40): não precisa adicionar essa linha, pois a
    # unica opção que sobra é acima de imc 40
    print("Seu IMC é {}, você está com Obesidade mórbida!!".format(imc))