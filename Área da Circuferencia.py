while True:
 raio = input ('Digite o valor do raio: ')

 try:
       num_1_float = float(raio)
       raio = True
 except:
     raio = None
    
 if raio is None:
       print('Digite apenas números')
       continue
   
 area = 3.14 * (num_1_float * num_1_float )
 
 print(f'a aréa da circuferência é: {area} cm²')

 sair = input ('Quer sair? [s]im: ').lower().startswith('s') 
    
 if sair is True:
    break