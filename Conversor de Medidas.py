while True:
   medida = input ('Digite [m] para converter metro para centimetro \nDigite [c] para converter centimetro para metro: ')
   operadores_permitidos = 'mc'
   
   if medida not in operadores_permitidos:
       print('Digite apenas M ou C')
       continue
   
   if medida =='m':
    valor_em_metro = input ('Digite o valor em metros (Exemplo: 52.20): ')
    valor_em_centimetro = 100
   
    try:
     num_1 = float(valor_em_metro)
     valor_em_metro = True

    except:
     valor_em_metro= None

    if valor_em_metro is None:
     print('Digite o valor correto')
     continue

    conversao_1 = int(valor_em_centimetro) * float(num_1)
   
    print(f'Em Centimetro é: {int(conversao_1)}cm')

   elif medida == 'c':
    valor_em_centimetro = input ('Digite o valor em centimetros 5220: ')
    valor_em_metro = 100
    
   try:
     num_2 = float(valor_em_centimetro)
     valor_em_centimetro = True

   except:
     valor_em_centimetro = None

   if valor_em_centimetro is None:
     print('Digite o valor correto')
     continue

   conversao_2 = float (num_2) / float(valor_em_metro)
  
   print(f'Em Metros é: {conversao_2}m')

   sair = input ('Quer sair? [s]im: ').lower().startswith('s') 
    
   if sair is True:
        break
      
      