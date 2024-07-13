'''
Faça um Programa que verifique se uma letra digitada
é vogal ou consoante.
'''
print('Digite uma letra para saber se é vogal ou consoante')
string_1 = input('Digite uma letra: ')

vogais ='aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'


if string_1 in vogais:
    print('A letra digitada é um vogal')

elif string_1 in consoantes:
  print('A letra digitada é uma consoante')

elif vogais and consoantes not in string_1:
   print('A informação digitada é uma palavra ou um número')