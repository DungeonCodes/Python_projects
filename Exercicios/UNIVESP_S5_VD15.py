altura = input('Digite a sua altura')
sexo = input('Digite h para homem e m para mulher')

alt = eval(altura)

if sexo == 'h':
    peso = (72.7*alt)-58
else:
    peso = (62.1*alt)-44.7
print('O peso idel e:', peso)
