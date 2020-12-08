# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 9:31:17 2020

@author: val <3
"""
try:
    numero = int(input("Hola, soy Mei, ¡Ingresa el número profavor!"))
    if numero>0 and numero<100000000000000000000000000000000:
       uno= (numero+1)
       dos= (numero+2)
       tres= (numero+3)
       suma=(uno+dos+tres)
       print("El total es de : ",suma)
    else: print("¡Woops! Ingresaste una cantidad demasiado grande o negativa, intentalo de nuevo")
except:
    print("¡Woops! Ingresaste una cantidad erronea, intentalo de nuevo")
