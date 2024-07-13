while True:
 numero_1 = input ('Digite o valor da área do quadrado\nExemplos: Valor em metros(20.0), Valor em centimetro(200): ')
 
 try:
   num_1_float = float (numero_1)
   numero_1 = True
 except:
   numero_1 = None

 if numero_1 is None:
     print('Digite o valor corretamente')
     continue
   
 area = (num_1_float * num_1_float)
 print(f'A área é {area:.2f}'.format(area),'cm²')

 sair = input ('Deseja sair? [s]im: ').lower().startswith('s') 

 if sair is True:
   break