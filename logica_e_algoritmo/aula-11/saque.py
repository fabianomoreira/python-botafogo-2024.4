resposta = 'S'

while resposta == 'S':
    valor = int(input('Qual valor para saque '))

    n50 = valor // 50
    n10 = (valor % 50) // 10
    n1  = (valor % 50) % 10

    print('Notas de 50 ', n50)
    print('Notas de 10 ', n10)
    print('Moedas de 1 ', n1)

    resposta = input('Deseja fazer outro saque (S/N)? ')
