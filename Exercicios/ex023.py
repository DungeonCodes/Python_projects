#numero = '8888'
#numero = str(input('Digite um número entre 0 e 9999'))
numero = int(input('Digite um número entre 0 e 9999'))
#esta dividindo por 1 e tirando o modulo por 10 (pega o resto da divisao por 10----->%10 e o resto da divisao por 10)
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero// 100%10
milhar = numero // 1000%10
print('unidade', unidade)
print('dezena:', dezena)
print('centena',centena)
print('milhar', milhar)
#print('centena:', centena)
#print('milhar:', milhar)






