#A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# - Até 9 anos : MIRIN
# - Até 14 anos : INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos : SÊNIOR
# - Acima: MASTER
from datetime import  date
ano = int(input("Qual o ano de nascimento:"))
idade = date.today().year - ano
if idade <=9:
    print("Atleta com {} anos, categoria MIRIM!".format(idade))
elif 10 <= idade <= 14:
    print("Atleta com {} anos, categoria INFANTIL!".format(idade))
elif 15 <= idade <= 19:
    print("Atleta com {} anos, categoria JUNIOR!".format(idade))
elif idade == 20:
    print("Atleta com {} anos, categoria SENIOR!".format(idade))
elif idade >= 21:
    print("Atleta com {} anos, categoria MASTER!".format(idade))
else:
    print("Não corresponde a uma categoria valida")
