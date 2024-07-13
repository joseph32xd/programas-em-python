tamanho_arquivo = float (input ('Digite o tamanho do arquivo para download em MB: '))
velocidade_internet = float (input('Digite a velocidade de link de internet em Mbps: '))

tempo_download = tamanho_arquivo / (velocidade_internet/8)

print(f'Com a velocidade de {velocidade_internet} Mbps,')
print(f'o download terá duração de {tempo_download:.1f} Minutos')