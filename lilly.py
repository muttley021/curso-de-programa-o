tamanho = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade de Internet (MBps): '))
print('Tempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) * 60) )
soma=(tamanho*8) / (velocidade*60)
print(soma)
