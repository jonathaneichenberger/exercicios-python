from math import sin, cos, tan, radians
anguloNormal = int(input('Digite um angulo qualquer: '))
angulo = radians(anguloNormal)
print('O seno de {} é igual a {:.3f}'.format(anguloNormal, sin(angulo)))
print('O cosseno de {} é igual a {:.3f}'.format(anguloNormal, cos(angulo)))
print('A Tangente de {} é igual a {:.3f}'.format(anguloNormal, tan(angulo)))
