while True:
 sexo = input ("Você é [M]ulher ou [H]omem: ")
 h = float(input('Digite sua altura: '))
 sexo_permitidos = 'mh' 

 if sexo not in sexo_permitidos:
   print('Digite corretamente se você é homem ou mulher!')
   continue
 
 if sexo == 'h': 
  peso_ideal_h = 72.20 * h - 58
  print(f'Seu peso ideal é: {peso_ideal_h:.1f}KG'.format(peso_ideal_h))
 
  sair = input ('Deseja [s]air: ').lower().startswith('s')

  if sair is True:
    break

 if sexo == 'm':
  peso_ideal_m = 62.1 * h - 44.7
  print(f'Seu peso ideal é: {peso_ideal_m:.1f}KG'.format(peso_ideal_m))

  sair = input ('Deseja [s]air: ').lower().startswith('s')

  if sair is True:
    break