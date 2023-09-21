area_para_pintar = float(input("Qual o tamanho em metros quadrados da area a ser pintada?"))
litro = area_para_pintar/6
latas = litro/18
galoes = litro/3.6
preco_lata =80
preco_galao = 25

if area_para_pintar < 18:
    print(" Você não pode comprar uma lata.")
    print(" Comprando galões de 3,6l, gastará R$ ", round(galoes) * preco_galao, ".")

else:
    print(" Se você comprar apenas latas de 18l, gastará R$ ", round(latas)*preco_lata, ".")
    print(" Se você comprar apenas galões de 3,6l, gastará R$ ", round(galoes)*preco_galao, ".")

## a partir daqui não está completo

mistura_lata = int(latas)
mistura_galao = int(galoes)

if area_para_pintar > mistura_lata:
    total_galao = area_para_pintar * mistura_galao
    print("Você utilizará", total_galao, "galões.")
else:
    total_misto = area_para


