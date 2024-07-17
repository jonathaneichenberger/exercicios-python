from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
print('Onde cateto oposto mede {} e o cateto adjacente mede {} a Hipotenusa mede {}'.format(co, ca, hypot(co, ca)))

