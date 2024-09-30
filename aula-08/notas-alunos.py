resposta = int(input('Quantos alunos para calcular?'))

i = 0

while i < resposta:
    nomeAluno = input('Digite o nome do aluno ')
    nota1 = float(input('Digite a primeira nota '))
    nota2 = float(input('Digite a segunda nota '))

    media = (nota1 + nota2)/2

    if (media >= 6.5):
        print(f"{media} - Aprovado")
    else:
        print(f"{media} - Reprovado")

    i = i + 1