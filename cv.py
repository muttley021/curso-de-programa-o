import math
area_da_pintura =  int(input("Informe o tamanho da área da pintura em m2: "))

galao = 3.6
lata_de_tinta = 18
preço_lata18litros = 80.00
preço_lata36litros = 25.00

quantidade_necessaria = area_da_pintura / 6

print(quantidade_necessaria)

galoesnecessarios = quantidade_necessaria / galao
latasnecessarias = quantidade_necessaria / lata_de_tinta
totalemlitros = (galoesnecessarios + latasnecessarias)
arredondado = math.ceil(totalemlitros)



print ("Galões necessários: {}".format(galoesnecessarios))
print ("Latas necessárias: {}".format(latasnecessarias))
print ("Litros de tinta necessários {:d}L".format(arredondado))
print ("Você vai precisar gastar: {:d}")