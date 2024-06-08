#crie um programa que leia o nome de uma pessoas e diga se ela tem "Silva" no nome.

nome = str(input('Qual e o seu nome')).strip()
print('Seu nome tem Silva?:{}'.format('silva' in nome.lower())