preço = float(input('Qual é o valor do produto? R$ '))
desconto = (preço * 5 / 100)
novo = preço - desconto
print(f'Seu produto agora custa {novo} $, pois teve 5% Off')