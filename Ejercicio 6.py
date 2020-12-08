# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:56:31 2020

@author: Val <3
"""
contador = 1

print(" ")
try:
    numero = int(input("Hola, soy Mei, ¡Ingresa el número profavor!"))
    
    while numero>20 or numero<=0:
        numero = int(input("Hola, soy Mei, ¡Ingresa el número profavor!"))
        contador += 1
    print (numero)
    print ("Intentos: ",contador)
except:
        print("¡Woops! Ingresaste una cantidad erronea, intentalo de nuevo")
    