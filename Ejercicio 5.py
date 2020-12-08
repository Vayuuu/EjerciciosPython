# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 00:50:44 2020

@author: Val <3
"""

print(" ")
print("Comprueba si un numero es menor a 20")
try:
    numero = int(input("Hola, soy Mei, ¡Ingresa el número profavor!"))
    
    while numero>20 or numero<=0:
            numero= int(input("Hola, soy Mei, ¡Ingresa el número profavor!"))
            
    print (numero)            
except:
    print("¡Woops! Ingresaste una cantidad erronea, intentalo de nuevo")
    
    
