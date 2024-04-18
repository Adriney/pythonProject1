#Faça um programa que leia o ano de nascimento de um
# jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo
# que falta ou que passou do prazo.
from  datetime import date
nasc= int(input("Digite o ano de su nascimento:"))
id =  date.today().year - nasc
id2 = id - 18
id3 = 18 - id
if id >18:
    print("Você possui {} anos e \033[33mja passou {} ano(s) do prazo\033[m de se alistar! ".format(id,id2))
elif id < 18:
    print("Você possui {} anos e \033[34mfalta {} ano(s)\033[m para poder se alistar! ".format(id, id3))
elif id == 18:
    print("Você possui {} anos e, \033[34mEstá no tempo\033[m  de se alistar! ".format(id))
