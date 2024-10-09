nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

if idade > 50:
    print(f"{nome} tem {idade} anos e é experiente")
else:
    print(f"{nome} tem {idade} anos e está em treinamento")