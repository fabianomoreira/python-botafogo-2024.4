alunos = []

for i in range(2):
    nome = input('Digite o nome: ')
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    media = (nota1 + nota2)/2
    resultado = "Aprovado" if media >= 6.5 else "Reprovado"

    alunos.append(
        {
            'nome': nome,
            'nota1': nota1,
            'nota2': nota2,
            'media': media,
            'resultado': resultado
        }
    )

print(alunos)