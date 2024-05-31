lp = float(input('Qual a largura da parede?'))
ap = float(input('Qual a altura da parede?'))
rt = float(input('Qual o rendimento da tinta por metro quadrado?'))
a = float(lp*ap)
lt = a/rt

print('Sua parede tem a dimensão de {}x{} e sua áre é de {}m2.'.format(lp, ap, a))
print('Para pintar sua parede , você precisará de {}l de tinta'.format(lt))