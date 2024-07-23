from random import randint
n = randint(0, 5)
print('O computador pensou em um número entre 0 e 5...')
print('Digite um número entre 0 e 5 e tente adivinhar!')
adivinhar = int(input('Seu palpite: '))
if adivinhar == n:
    print('Parabéns você acertou!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(n, adivinhar))
