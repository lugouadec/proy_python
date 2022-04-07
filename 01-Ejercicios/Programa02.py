tc = input("¿Ingresa el total de tu compra? : ")
#print (type(tc))
descueto =  float(tc) * 0.15
total_a_pagar = float(tc) - descueto
print (f"El total a pagas es : $ {total_a_pagar:,.2f}")
