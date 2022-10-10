Sueldo_Basico = float(input("Ingrese el Sueldo basico..."))
Cantidad_Años = int(input("Ingrese los años de antiguedad..."))
Casado = int(input("Ingrese 1 si usted es casado o 0 Si esta soltero"))
Hijos = int(input("Ingrese 1 si usted tiene hijos o 0 Si no tiene hijos"))
Cantidad_Hijos = float(input("Ingrese la cantidad de hijos..."))
Result_D = Sueldo_Basico / 0.012
Final = Result_D * Cantidad_Años
Final_1 = Final + Sueldo_Basico
Aporte_Jubilatorio = Sueldo_Basico * 0.11 
Obra_Social = Sueldo_Basico * 0.03
Aport_grem = Sueldo_Basico * 0.01
if Casado == 1:
 Activo_cony = 8000
 Suma_1 = Final_1 - Aporte_Jubilatorio - Obra_Social - Aport_grem + Activo_cony
 print("Sueldo basico" + Sueldo_Basico)
 print("Activos por antiguedad" + Final)
 print("Descuento por juvilacion" + Aporte_Jubilatorio)
 print("Dedscuento por obra social" + Obra_Social)
 print("Descuento por aporte gremial" + Aport_grem)
 print("Activo por tener conyuje" + Activo_cony)
 print("Sueldo Neto" + Suma_1)
elif Casado == 0:
  print("El dinero  no se sumara a su sueldo porque no esta casado")
  Suma_1 = Final_1 - Aporte_Jubilatorio - Obra_Social - Aport_grem 
  print("Sueldo basico" + Sueldo_Basico)
  print("Activos por antiguedad" + Final)
  print("Descuento por juvilacion" + Aporte_Jubilatorio)
  print("Dedscuento por obra social" + Obra_Social)
  print("Descuento por aporte gremial" + Aport_grem)
  print("Sueldo Neto" + Suma_1)
elif Hijos == 1:
    Aporte_Hijos = 4000 
    Suma_2 = Final_1 - Aporte_Jubilatorio - Obra_Social - Aport_grem + Aporte_Hijos
    print("Sueldo basico" + Sueldo_Basico)
    print("Activos por antiguedad" + Final)
    print("Descuento por juvilacion" + Aporte_Jubilatorio)
    print("Dedscuento por obra social" + Obra_Social)
    print("Descuento por aporte gremial" + Aport_grem)
    print("Activo por tener conyuje" + Aporte_Hijos)
    print("Sueldo Neto" + Suma_2)
elif Hijos == 0:
    print("El dinero  no se sumara a su sueldo porque no tiene hijos") 
    Suma_2 = Final_1 - Aporte_Jubilatorio - Obra_Social - Aport_grem
    print("Sueldo basico" + Sueldo_Basico)
    print("Activos por antiguedad" + Final)
    print("Descuento por juvilacion" + Aporte_Jubilatorio)
    print("Dedscuento por obra social" + Obra_Social)
    print("Descuento por aporte gremial" + Aport_grem)
    print("Sueldo Neto" + Suma_2)




