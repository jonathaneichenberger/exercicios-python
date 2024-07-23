n1 = int(input('Digite o 1º Valor: '))
n2 = int(input('Digite o 2º Valor: '))
n3 = int(input('Digite o 3º Valor: '))

maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
