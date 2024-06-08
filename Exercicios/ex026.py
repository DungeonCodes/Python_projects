#Crie um programa que leia o numero de ocorrencias de uma letra, a posicao que a primeira o corre e a ultima

frase = str(input('Digite uma frase:')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('a')+1))
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('a')+1))