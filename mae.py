distância = float(input("Digite a distância em km:"))
velocidade_média = float(input("Digite a velocidade média em km/h:"))
tempo = distância / velocidade_média
#calculando as horas
#diminuir a velocidade
# Opcional: imprimir o tempo em horas, minutos e segundos
tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
horas = int(tempo_s / 3600)  # parte inteira
tempo_s = int(tempo_s % 3600)  # o resto
minutos = tempo_s / 60
segundos = int(tempo_s % 60)
print("%02d:%02d:%02d" % (horas, minutos, segundos))
#primeiro pedi pro o usuario digitar a distancia e a velocidade media depois convertir as horas os minutos e os segundo depois so somei tudo





