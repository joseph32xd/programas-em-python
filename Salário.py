while True:
 salario_hora = float (input('Quanto você ganha por hora: R$'))
 horas_trabalhadas = float(input('Digite o total de horas trabalhadas: '))

 salario_bruto = salario_hora * horas_trabalhadas

 imposto_renda = salario_bruto * 11 / 100
 inss = salario_bruto * 8 / 100
 sindicado = salario_bruto * 5 / 100
 salario_liquido = salario_bruto - imposto_renda - inss - sindicado

 desconto_total = imposto_renda + inss + sindicado

 print(f'O Salário bruto é: R${salario_bruto}')

 print('Impostos descontados')

 print(f'O valor pago de 8% para o INSS é: R${inss:.2f}')
 print(f'O valor pago de 11% para o imposto de renda é: R${imposto_renda:.2f}')
 print(f'O valor pago de 5% para o sindicado é: R${sindicado:.2f}')
 print(f'O seu salario liquido do mês é: R${salario_liquido:.2f}')
 print(f'Foi descontado um total de: R${desconto_total:.2f}')

 sair = input('Deseja [S]air:').lower().startswith('s')

 if sair is True:
  break
