from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
print('Onde cateto oposto mede {:.2f} e o cateto adjacente mede {:.2f} a Hipotenusa mede {:.2f}'.format(co, ca, hypot(co, ca)))

