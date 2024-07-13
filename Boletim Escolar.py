while True:
   numero_1 = input ('Digite a nota da Prova Bimestral (0 a 10): ')
   numero_2 = input ('Digite a nota do Trabalho Bimestral (0 a 10): ')
   numero_3 = input ('Digite a nota do Leque (0 a 10): ')
   numero_4 = input ('Digite a nota da Prova Institucional (0 a 10): ')
   
   numeros_validos = None
   
   try:
      num_1_float = float (numero_1)
      num_2_float = float (numero_2)
      num_3_float = float (numero_3)
      num_4_float = float (numero_4)
      numeros_validos = True
   except:
      numeros_validos = None
   
   if numeros_validos is None:
       print('Um ou todas as notas foram digitadas incorretamente.')
       continue
   
   media_bimestral = (num_1_float + num_2_float + num_3_float + num_4_float)/4

   if media_bimestral >= 7:
      print(f'Sua nota é: {media_bimestral} \nVocê está aprovado')

   elif media_bimestral <= 7:
      print(f'Sua nota é: {media_bimestral} \nVocê está reprovado')

   sair = input ('Quer sair? [s]im: ').lower().startswith('s') 
    
   if sair is True:
        break
      

