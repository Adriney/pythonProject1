#Faça um programa que leia o sexo de uma pessoa, mas só aceite
# os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.


sexo = input('Digite o sexo (M/F):').upper()


# Entra em um loop enquanto a entrada do usuário não for 'M' ou 'F'
while sexo not in ['M', 'F']:
    # Se a entrada do usuário não for válida,
    # solicita novamente o sexo e atualiza a entrada convertendo para maiúsculas
    sexo = input(f'Você digitou {sexo},Valor digitado incorreto.'
                 f'\n Digite o sexo novamente(M/F):').upper()
# Quando o loop termina, significa que a entrada do usuário é válida,
# então imprime a mensagem indicando que o sexo é válido
print('Sexo válido, você digitou:',sexo)
