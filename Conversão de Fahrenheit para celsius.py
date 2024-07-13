while True:
 valor_usuario = input ('Digite a temperatura em fahremheit: ').replace('F°','')
   
 try:
   num_1 = float(valor_usuario)
   valor_usuario = True

 except:
   valor_usuario = None

 if valor_usuario is None:
   print('Digite o valor correto')
   continue

 celsius = (num_1 - 32) * (5/9)

 print(f'A temperatura é: {celsius:.1f}C°'.format(celsius))

 sair = input ('Você deseja [s]air: ').lower().startswith('s')

 if sair is True:
  break