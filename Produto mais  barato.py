produto_1 = float (input('Digite o preço do produto 1: R$'))
produto_2 = float (input('Digite o preço do produto 2: R$'))
produto_3 = float (input('Digite o preço do produto 3: R$'))

if produto_1 < produto_2 and produto_3:
    print('O produto 1 é o mais barato, portanto compre-o')

elif produto_2 < produto_1 and produto_3:
    print('O produto 2 é o mais barato, portanto compre-o')

elif produto_3 < produto_1 and produto_2:
    print('O produto 3 é o mais barato, portanto compre-o ')

elif produto_1 == produto_2 and produto_3:
    print('Os valores são os mesmos!')