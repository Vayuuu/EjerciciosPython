# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:19:33 2020

@author: Val <3
"""
try:
    suma=0
    numero = int(input("Hola, soy Mei, ¡Ingresa el número profavor!"))
    if numero>0 and numero<100000000000000000000000000000:
        suma+= numero
        while numero!=0:
            numero = int(input("Hola, soy Mei, ¡Ingresa el número profavor!"))
            suma+= numero 
        print ("Total:",suma)
    else:
        print("¡Woops! Ingresaste una cantidad muy grande o negativa, intentalo de nuevo")
except:
    print("¡Woops! Ingresaste una cantidad erronea, intentalo de nuevo")
    
    