perguntas = [
     {
       'Pergunta':'Quanto é 9x9 ?',
       'Opções':['67', '32', '85', '81'],
       'Resposta':'81',
},
   {
       'Pergunta' : 'Quanto é √144 ?',
       'Opções' : ['12', '45', '56', '80'],
       'Resposta': '12',
},
   {
       'Pergunta': 'Quanto é 34 - 56 ?',
       'Opções' : ['-89', '-51', '-22', '-32'],
       'Resposta' : 'C) -22'
},
   {
       'Pergunta': 'Quanto é 2 x = 20 ?',
       'Opções': ['2', '10', '8', '6'],
       'Resposta': '10',
   }
]

qtd_acertos = 0
for pergunta in perguntas:
    print(f'Pergunta:', pergunta['Pergunta'])
    print()

    opcoes= pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}', opcoes)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    if escolha .isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_acertos:
            if opcoes[escolha_int] == pergunta ['Resposta']:
               acertou = True

    print()
    if acertou:
     qtd_acertos += 1
     print('Acertou 😊')
    else:
     print('Errou 😢')
    
    print()

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
