while True:
  fator_1 = input ('Qual tabuada você quer: ')
  fator_2 = 0

  try:
     num_1 = int(fator_1)
  except:
     fator_1 = None
     
     if fator_1 is None:
        print('Digite apenas números inteiros')
        continue
    
  while fator_2 < 10:
     fator_2 += 1
     produto = (num_1 * fator_2)
     print(f'{num_1} x {fator_2} = {produto}')

  sair = input ('Você deseja sair: ').lower().startswith('s')

  if sair is True:
     break