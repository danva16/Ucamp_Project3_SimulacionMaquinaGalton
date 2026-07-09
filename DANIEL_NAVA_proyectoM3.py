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
        #inicializamos la posición de la canica en la posición central alta (12) de los 24 contenedores, ya que la posición 0 es la extrema izquierda y la posición 23 es la extrema derecha
        contenedor_actual = 12
        #cada canica pasa por 12 niveles de obstáculos
        for nivel in range(total_niveles):
            #generamos un número aleatorio entre 0 y 1 como es el estándar, simulando si va a la izquierda o la derecha
            desicion = random.random()
            #con un if especificamos que se realiza si va a la derecha o a la izquierda, si es mayor a 0.5 va a la derecha y si es menor o igual a 0.5 va a la izquierda
            if desicion > 0.5:
                contenedor_actual += 1 #si va a la derecha se le suma 1 a su posición
            else:
                contenedor_actual -= 1 #si va a la izquierda se le resta 1 a su posición
        #cuando la canica termina de pasar los 12 niveles, guardamos su contenedor final
        resultados_contenedores.append(contenedor_actual)
    #devolvemos la lista con los contenedores finales de cada canica
    return resultados_contenedores
#creamos nuestra función para mostrar nuestro gráfico con matplotlib
def graficar_histograma(resultados):
    #creamos nuestro gráfico y definimos su tamaño
    plt.figure(figsize=(10, 6))
    #dibujamos nuestro gráfico y le damos el estilo de barras, además de definir el color y el ancho de las barras
    #almacenamos el resultado del grafico en variables
    #'cuentas' es la cantidad de canicas que cayeron en cada contenedor y 'cajas' son las posiciones de las barras en el eje X
    cuentas, cajas, _ = plt.hist(resultados, bins=range(0, 26), color='#66B2FF', edgecolor='#FF0000', align='left')
    #con un for recorremos cada barra del gráfico y añadimos el número de canicas que cayeron en cada contenedor encima de cada barra
    for cantidad, posicion in zip(cuentas, cajas):
        #solo ponemos el número si es mayor de 0
        if cantidad > 0:
            plt.text(posicion, cantidad + 5, str(int(cantidad)), ha='center', va='bottom', fontsize=12, color="#ff0000")
    #establecemos el título de nuestro gráfico y nombre a los ejes
    plt.title('Simulación de la Máquina de Galton', fontsize=22, fontweight='bold')
    plt.xlabel('Distribución de las Canicas', fontsize=20)
    plt.ylabel('Cantidad de Canicas', fontsize=20)
    #añadimos los números de cada contenedor debajo de cada barra para mostrar en que contenedor quedaron las canicas
    plt.xticks(range(0, 25))
    #por último mostramos nuestro gráfico
    plt.show()
#hacemos el llamado de nuestras funciones para simular las canicas y graficar el histograma
resultados = simular_canicas()
graficar_histograma(resultados)