while True:
 salario_hora = (input ('Quanto você ganha por hora?: ').replace('R$',' '))
 horas_trabalhadas = (input ('Quantas horas você trabalhou no Mês?: '))
 mes = input ('Qual mês você trabalhou?: ')

 try:
    num_1_float = float(salario_hora)
    num_2_float = float(horas_trabalhadas)
    numeros_validos = True
 except:
   numeros_validos = None

 if numeros_validos is None:
       print('Digite apenas números')
       continue

 salario_total = num_1_float * num_2_float
 
 print(f'Seu salário de {mes} vai ser: R${salario_total:.2f}'.format(salario_total))

 sair = input ('Quer sair? [s]im: ').lower().startswith('s') 
    
 if sair is True:
        break
      