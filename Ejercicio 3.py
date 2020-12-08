# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:51:24 2020

@author: Val <3
"""


continuar = True
while continuar:
    while True:
         try:
             print(" ")
             print("Comprueba si tu compra tiene descuento")
             monto= int(input("Hola, soy Mei, ¡Ingresa el monto de tu compra! : $ "))          
             if monto<=1000000:
                 if monto>0:
                     mes=str(input("Ingesa el mes actual(Ej. Enero/enero):"))
                     if mes=="Octubre" or mes=="octubre":
                         total=monto-(monto*0.15)
                         print("El monto mas el descuento da un total de $",total)
                     else:
                         if mes=="Enero" or mes=="enero":
                             print("No existe descuento para la compra, el total es de",monto)
                         else:
                             if mes=="Febrero" or mes=="febrero":
                                 print("No existe descuento para la compra, el total es de",monto)
                             else:
                                 if mes=="Marzo" or mes=="marzo":
                                     print("No existe descuento para la compra, el total es de",monto)
                                 else:    
                                     if mes=="Abril" or mes=="abril":
                                         print("No existe descuento para la compra, el total es de",monto)
                                     else:
                                         if mes=="Mayo" or mes=="mayo":
                                             print("No existe descuento para la compra, el total es de",monto)
                                         else:
                                             if  mes=="Junio" or mes=="junio":
                                                 print("No existe descuento para la compra, el total es de",monto)
                                             else:
                                                 if mes=="Julio" or mes=="julio":
                                                     print("No existe descuento para la compra, el total es de",monto)
                                                 else:
                                                     if mes=="Agosto" or mes=="agosto":
                                                         print("No existe descuento para la compra, el total es de",monto)
                                                     else:
                                                         if mes=="Septiembre" or mes=="septiembre":
                                                             print("No existe descuento para la compra, el total es de",monto)
                                                         else:
                                                             if mes=="Noviembre" or mes=="noviembre":
                                                                 print("No existe descuento para la compra, el total es de",monto)
                                                             else:
                                                                 if mes=="Diciembre" or mes=="diciembre":
                                                                     print("No existe descuento para la compra, el total es de",monto)
                                                                 else: 
                                                                     print("No existe ese mes")
                 else:    
                    print("No se ha ingresado ninguna cantidad")
             else:
                 print("¡No se admiten compras de más de $1,000,000!")           
         except ValueError:
             print("¡Woops! Ingresaste una cantidad erronea, intentalo de nuevo")
         break
continuar = ("s" == input("").lower())