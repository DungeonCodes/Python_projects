produto = float(input('Qual é o preço do produto?R$'))
desconto = 5
venda = (produto*(100-desconto))/100

print('O produto que custava R${:.2f} na promoção com desconto de {} vai custar R${:.2f}.'.format(produto,desconto,venda))