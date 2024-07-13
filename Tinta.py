tamanho_area = float(input ('Qual o tamanho da área em quadrados que vai ser pintada: '))

litros = tamanho_area * 1 / 3
valor_em_litros = litros * 80 / 18

print (f'A quantidade de litros necessária  para pintar a área de {tamanho_area}m² é de {litros:.0f} litros')
print(f'O valor total é de R${valor_em_litros:.2f}')