#Escreva um programa que leia um número n inteiro qualquer e mostre
# na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0->1->1->2->3->5->8
n = int(input('Digite o número de lementos da Sequancia de Fobonacci'
              '\n que você deseja ver:'))
fibonacci = [0, 1]

if n <= 0:
    print('Por favor, insira um número inteiro positivo maior que zero.')
elif n == 1:
    print('Sequência de Fibonacci com 1 elemanto:', fibonacci[0])
else:
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        print('Sequencia de Fibonacci com', n, 'elementos:')
        for num in fibonacci:
            print(num, end='->')