h = float(input('Digite a sua altura : '))
sexo = input('Informe o sexo (M/F) : ')

if (sexo == 'M'):
    peso = (72.7*h)-58
else:
    peso = (62.1*h)-44.7

print('O seu peso ideal é ', peso)