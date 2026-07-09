# Simulación de la Máquina de Galton
# importamos las librerías necesarias
import random
import matplotlib.pyplot as plt
# simulamos el paso de las canicas por los niveles de obstáculos
#devuelve una lista con el contenedor final de cada canica
def simular_canicas(total_canicas=3000, total_niveles=12):
    #creamos una lista para almacenar el contenedor final de cada una de las 3000 canicas
    resultados_contenedores = []
    #bucle para simular el paso de cada canica por los niveles de obstáculos
    for canica in range(total_canicas):
        #inicializamos la posición de la canica en la posición central alta (0)
        contenedor_actual = 0
        #cada canica pasa por 12 niveles de obstáculos
        for nivel in range(total_niveles):
            #generamos un número aleatorio entre 0 y 1 como es el estándar, simulando si va a la izquierda o la derecha
            desicion = random.random()
            #con un if especificamos que se realiza si va a la derecha o a la izquierda, si es mayor a 0.5 va a la derecha y si es menor o igual a 0.5 va a la izquierda
            if desicion > 0.5:
                #con un if especificamos que se realiza cuando la posición de la canica esta en la posición a la extrema derecha o en otro
                if contenedor_actual == 11: #si se encuentra a la extrema derecha no se le permite ir a la derecha y se queda en la misma posición
                    contenedor_actual += 0
                else: 
                    contenedor_actual += 1 #si se encuentra en cualquier otra posición se le permite ir a la derecha y se le suma 1 a su posición
            else: 
                if contenedor_actual == 0: #si se encuentra a la extrema izquierda no se le permite ir a la izquierda y se queda en la misma posición
                    contenedor_actual += 0
                else:
                    contenedor_actual -= 1 #si se encuentra en cualquier otra posición se le permite ir a la izquierda y se le resta 1 a su posición
        #cuando la canica termina de pasar los 12 niveles, guardamos su contenedor final
        resultados_contenedores.append(contenedor_actual)
    #devolvemos la lista con los contenedores finales de cada canica
    return resultados_contenedores
