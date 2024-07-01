#Crie um porgrama que identifique o primeiro e o ultimmo nome

'''
#Minha resolucao sem ver a resposta
nome = str(input('Digite seu nome completo')).strip()
primeiro_espaco = nome.find(' ')
primeiro_nome = (nome[0:primeiro_espaco])
ultimo_espaco = nome.rfind(' ')
comprimento = (len(nome))
sobrenome = (nome[ultimo_espaco:comprimento])
print('Muito prazer em te conhecer! \n Seu primeiro nome e {} \n Seu ultimo nome e {}'.format(primeiro_nome,sobrenome))
'''

#Resolucao do professor
n = str(input('Pessoa 2 digite seu nome completo')).strip()
nome2 = n.split()
print('Seu primeiro nome e {}'.format(nome2[0]))
print('Seu ultimo nome e {}'.format(nome2[len(nome2)-1]))

