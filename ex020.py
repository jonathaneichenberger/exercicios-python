from random import sample
aluno1 = str(input('Digite o nome do primeiro Aluno: '))
aluno2 = str(input('Digite o nome do primeiro Aluno: '))
aluno3 = str(input('Digite o nome do primeiro Aluno: '))
aluno4 = str(input('Digite o nome do primeiro Aluno: '))

print('O nome sorteado foi {} '.format(sample([aluno1, aluno2, aluno3, aluno4], k=4)))
