s1 = float(input('Digite o 1º Segmento: '))
s2 = float(input('Digite o 2º Segmento: '))
s3 = float(input('Digite o 3º Segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os Segmentos digitados podem formar um triângulo!')
else:
    print('Os Segmentos digitados NÃO podem formar um triângulo!')