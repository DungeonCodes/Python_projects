frase = 'Curso em Vídeo Python   '
print(frase[0:15:2])
print(""""ajklshdfhjklsjdhfkjhskdhfhsdfhsahkjhjkhkjhj

khjkhjkhhjkhjkhjkhhhjkhjkhjkhjkjkhjkhhkhh""")
print(frase.count('o'))#count conta quantas vezes apareceu aquele caractere
print(frase.upper().count('O'))#upper deixa a string em maiusculo
print(len(frase))#len conta quantos caracteres tem a string
print(len(frase.strip()))#strip retira os espacos antes e depois da string
print(frase.replace('Python', 'Android'))#replace substitui o antigo pelo novo
print(frase)
#frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.find('Vídeo'))#find encontra aquela string dentro de outra string se eu quiser alterar a posicao posso usar +1

print(frase.lower().find('vídeo'))
print(frase.split())#split separa a string pelos espacos
dividido = frase.split()
print(dividido[2])
print(dividido[2][3])
#Pular linha no meio do .format    \n
