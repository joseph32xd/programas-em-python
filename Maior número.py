'''
Faça um Programa que peça um valor e mostre na tela 
se o valor é positivo ou negativo.
'''
num_1 = input ('Digite o primeiro número: ')
num_2 = input ('Digite o segundo número: ')

if num_1 > num_2:
    print(f'{num_1} B) É o maior número ')

elif num_2 > num_1:
    print(f'{num_2} A) É o maior número')

elif num_1 == num_2:
    print('Ambos números são iguais')


