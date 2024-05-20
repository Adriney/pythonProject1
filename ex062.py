#Melhore o DESAFIO 61, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar 0 termos.


while True:
    print('==' * 12)
    print('  10 TERMOS DE UMA PA  ')
    print('==' * 12)
    primeiro = int(input('Primeiro termo:'))
    razão = int(input('Razão:'))
    termo = primeiro
    cont = 1  # Inicializa o contador em 1 para contar os termos

    while cont <= 10:# Enquanto o contador for menor ou igual a 10
        print(f'{termo}', end=' -> ')
        termo += razão # Calcula o próximo termo da PA
        cont += 1 # Incrementa o contador
    opcao = int(input('\nDeseja mostrar mais termos?\n(Digite 0 para encerrar):'))
    if opcao == 0:
        print('Encerrando programa.')
    else:
        print('Opção  digitada é invalida!')
        continue