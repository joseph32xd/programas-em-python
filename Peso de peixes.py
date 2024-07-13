'''
João Papo-de-Pescador, homem de bem, comprou um
microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo
excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na
variável excesso a quantidade de quilos além do limite e na
variável multa o valor da multa que João deverá pagar. Imprima
os dados do programa com as mensagens adequadas.
'''
peso_dos_peixes = float(input('Digite o peso total dos peixes: '))
peso_limite = 50.01
multa = 4

if peso_dos_peixes >= peso_limite:
    calculo_da_multa = (peso_dos_peixes - 50) * multa
    print(f'O peso dos peixes ultrapassa o limite \nPortanto o valor da multa será de: R${calculo_da_multa:.2f}')

elif peso_dos_peixes < peso_limite:
    print('O peso está dentro do limite')