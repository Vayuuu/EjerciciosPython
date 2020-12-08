# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:34:20 2020

@author: Val <3
"""

continuar = True
while continuar:
    while True:
         try:
             print(" ")
             print("Taquilla del parque de diversiones")
             edad = int(input("Hola, soy Mei, ¡Ingresa tu edad por favor! : "))          
             if edad<=120:
                 if edad>0:
                     if edad<10:
                             total=(50*0.75)
                             print ("El precio de tu boleto es de $",total," soles")
                     else:                               
                             print ("El precio de tu boleto es de $50 soles")
                 else: 
                    print("¡No puedes tener menos de 0 años!")
             else:
                 print("¡No puedes tener más de 120 años!")
                 
         except:
             print("¡Woops! Ingresaste una cantidad erronea, intentalo de nuevo")
         break
continuar = (input("").lower())
