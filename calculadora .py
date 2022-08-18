def function (valor_dolar, nombre_moneda):
   moneda = int(input("¿cuantos " + nombre_moneda + " tienes? : " ))
   dolares = moneda / valor_dolar
   dolares = round (dolares , 2)
   dolares = str (dolares)
   print ("tienes " +dolares+ " dolares")
menu = int(input ("""

bienvenido al convertidor de monedas:
porfavor elige que moneda deseas convertir a dolar

1: pesos colombianos
2: pesos argentinos
3: pesos mexicanos

"""))

if menu == 1:
    function (3555, "pesos colombianos")

elif menu == 2:
    function (2344, "pesos argentinos")
        
elif menu == 3:
    function (1223, "pesos mexicanos")

else:
    print("porfavor ingresa un numero valido")

