while True:
 valor_usuario = input ('Digite a temperatura em celsius: ').replace('C°','')
   
 try:
   num_1 = float(valor_usuario)
   valor_usuario = True
   
 except:
   valor_usuario = None

 if valor_usuario is None:
   print('Digite o valor correto')
   continue

 fahrenheit = num_1 * 1.8 + 32

 print(f'A temperatura é: {fahrenheit:.1f}F°'.format(fahrenheit))

 sair = input ('Você deseja [s]air:').lower().startswith('s')

 if sair is True:
    break