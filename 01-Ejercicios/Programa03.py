cal1 = float(input("¿Ingresa la calificacion No 1: "))
cal2 = float(input("¿Ingresa la calificacion No 2: "))
cal3 = float(input("¿Ingresa la calificacion No 3: "))
ef = float(input("¿Ingresa la calificacion del examen Final: "))
tf = float(input("Ingresa la calificacion del Tranajo Final: "))

promedio = (cal1+cal2+cal3)/3
ppar = promedio * 0.55
pef = ef * 0.30
ptf = tf * 0.15
cf = ppar + pef + ptf
print (f"Tu calificacion Final es : {cf:,.2f}")
