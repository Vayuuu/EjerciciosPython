# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 13:15:49 2020

@author: Val <3
"""

continuar = True
while continuar:
    while True:
         try:
             print(" ")
             print("Calculadora de sueldo total")
             sueldo = int(input("Hola, soy Mei, ¡Ingresa tu sueldo porfavor! : $"))          
             if sueldo<=75400000:
                 if sueldo>0:
                     if sueldo>=4000:
                             total=(sueldo*0.15)+sueldo
                             print ("Tu sueldo es de $",total)
                     else:  
                             total=(sueldo*0.08)+sueldo
                             print ("Tu sueldo es de $",total)
                 else: 
                    print("¡No puedes ingresar numeros menores a 0!")
             else:
                 print("Tu sueldo no puede pasar de 75400000.00 que es el mas alto del mundo")
                 
         except ValueError:
             print("¡Woops! Ingresaste una cantidad erronea, intentalo de nuevo")
         break
continuar = ("s" == input("").lower())