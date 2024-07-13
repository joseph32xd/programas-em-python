while True:
  nome_do_aluno = input ('Seu Nome: ')
  peso_do_aluno = input ('Seu peso: ')
  altura_do_aluno =input('Sua altura: ')
  numeros_validos = None
   
  try:
      num_1_float = float (peso_do_aluno)
      num_2_float = float (altura_do_aluno)
      numeros_validos = True
  except:
      numeros_validos = None
   
  if numeros_validos is None:
       print('Seu peso ou altura foram digitas incorretamente')
       continue
   
  imc = num_1_float/ (num_2_float**2)

  if imc <= 16.9:
    print(f'{nome_do_aluno}, seu IMC é: {imc:.2f}'.format(imc),'\nPortanto você está muito abaixo do peso')
   
  elif 17 <= imc and imc <= 18.4:
    print(f'{nome_do_aluno}, seu IMC é: {imc:.2f}'.format(imc),'\nPortanto você está abaixo do peso')
  
  elif 18.5 <= imc and imc <= 24.9:
    print(f'{nome_do_aluno}, seu IMC é : {imc:.2f}'.format(imc),'\nPortanto você está com o peso normal')
  
  elif 25 <= imc and imc <= 29.9:
    print(f'{nome_do_aluno}, seu IMC é: {imc:.2f}'.format(imc),'\nPortanto você está acima do peso')

  elif 30 <= imc and imc <= 34.9:
    print(f'{nome_do_aluno}, seu IMC é: {imc:.2f}'.format(imc),'\nPortanto você está com Obesidade Grau I')

  elif 35 <= imc and imc <= 40:
    print(f'{nome_do_aluno}, seu IMC é: {imc:.2f}'.format(imc),'\nPortanto você está com Obesidade Grau II')
  
  elif imc >= 40:
    print(f'{nome_do_aluno}, seu IMC é: {imc:2f}'.format(imc),'\nPortanto você está com Obesidade Grau III')

  sair = input ('Quer sair? [s]im: ').lower().startswith('s') 
    
  if sair is True:
        break
      