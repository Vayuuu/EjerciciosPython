# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:20:29 2020

@author: Val <3
"""

print(" ")
print("Comprueba si un numero es menor a 10")
try:
    numero = int(input("Hola, soy Mei, ¡Ingresa el número profavor!"))
    
    while numero>=10 and numero<0:
        
            numero= int(input("Hola, soy Mei, ¡Ingresa el número profavor!"))
            
    print (numero)            
except:
    print("¡Woops! Ingresaste una cantidad erronea, intentalo de nuevo")
    

