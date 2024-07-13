'''
Faça um Programa que verifique se uma letra 
digitada é "F" ou "M". 
Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido.
'''
while True:
 sexo = input ('Digite o sexo: ')
 sexos_permitidos = 'mf'

 if sexo not in sexos_permitidos:
    print('Sexo inválido')
    continue

 if sexo == 'm':
   print('M é Masculino')
   break

 elif sexo == 'f':
   print('F é feminino')