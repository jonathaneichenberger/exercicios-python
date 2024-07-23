numero = int(input('Digite um número qualquer: '))
par_ou_impar = numero % 2
if par_ou_impar == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))