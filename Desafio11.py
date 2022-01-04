base = float(input('Quantos metros tem a largura da parede? '))
altura = float(input('Quantos metros tem de altura? '))
parede = base*altura #em cm², para converter, utilize 10.000 cm²
tinta = parede / 2 #utiliza-se 1 litro de tinta para pintar 2m² de parede
print(f'Com uma parede de {parede:.1f} M², podemos pintá-la com {tinta:.1f} Litros de tintas !')
