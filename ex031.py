km = float(input('Quantos km de distância será sua viagem? '))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('O preço da sua viagem será de R$:{:.2f}'.format(preco))
