salario = float(input('Qual é o salário do funcionário? R$:'))
if salario <= 1250:
    novo_salario = salario * 1.15
else:
    novo_salario = salario * 1.10
print('Seu salário era de R$:{:.2f} e agora passou a ser R$:{:.2f}'.format(salario, novo_salario))