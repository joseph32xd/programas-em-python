'''
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
nota_1 = float (input('Digite a primeira nota (0 a 10): '))
nota_2 = float (input('Digite a segunda nota (0 a 10): '))

media = (nota_1 + nota_2)/ 2

if media <= 6.9:
    print(f'Reprovado {media}')

elif 7<= media <= 9.5:
    print(f'Aprovado {media}')

elif media == 10:
    print(f'Aprovado por Distinção {media} ')
