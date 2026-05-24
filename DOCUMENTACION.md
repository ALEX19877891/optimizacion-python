## CULTURA DIGITAL Y SOCIEDAS
## Actividad Autónoma 4
# Unidad 2: Herramientas y Metodologías en Ciencia de Datos
# Nombre: Alex Chicaiza
# Optimización de Código en Python utilizando NumPy y Profiling


---

# Introducción

La presente tarea autonoma tiene como objetivo analizar y optimizar un algoritmo en Python encargado de encontrar números primos entre 1 y 100000.

Como primer paso se realizo un código original basico sin optimizaciones, el cual tenia problemas de rendimiento debido al mal uso de interacciones y algunas validaciones que era innecearias.

Posterior se realizo un analizar minicioso cada parte del programa y se observo que se podia reducir sesgos encontrados en el  desarrolo los cuales se rectifico y se logro optimizar el codigo y mejorar el tiempo de ejecucion.

## Código Original

El archivo utilizado fue nombrano como `codigo_original.py` implementa un algoritmo básico para encontrar números primos.

El principal problema identificado fue el uso excesivo de iteraciones dentro del ciclo de validación de números primos.

### Captura código original y su resultado

![Codigo Original](imagenes/imagen1.png)

--------------------------

##  Optimización del Código

 # GIT Y GITHUB
Creacion del repositorio
Se creó el repositorio optimizacion-python en GitHub para almacenar y gestionar las versiones del proyecto mediante Git.
Se creó una nueva rama en Git denominada optimizacion-codigo para trabajar las mejoras del proyecto sin afectar la rama principal.

![Ceaccion del repositotio](imagenes/imagen2.png)

Se creó una nueva rama en Git denominada optimizacion-codigo para trabajar las mejoras del proyecto sin afectar la rama principal.


![Ceaccion de la rama](imagenes/imagen3.png)



# Optimización

Para mejorar el rendimiento del algoritmo se aplicaron las siguientes técnicas:

## Reducción de iteraciones

Se utilizó la función `math.sqrt()` para reducir el número de iteraciones necesarias durante la validación de números primos.

## List Comprehensions

Se implementaron list comprehensions para optimizar la creación de listas y mejorar la velocidad del procesamiento.

## Arrays NumPy

Se utilizó `np.arange()` para generar arrays numéricos de forma más eficiente que las listas tradicionales de Python.

### Captura código optimizado

![Codigo Optimizado](imagenes/imagen4.png)

---------------------------------------
# Crear commit



Se realizó el primer commit del proyecto utilizando Git, almacenando la versión inicial del código original.

![Primer commit](imagenes/imagen5.png)

---

# Resultados

Se compararon los tiempos de ejecución entre el código original y el código optimizado.

Los resultados demostraron una mejora significativa en el rendimiento del algoritmo optimizado.

## Comparativa de tiempos

| Version | Tiempo |
|---|---|
| Codigo Original | 25 segundos |
| Codigo Optimizado | 2 segundos |

## Analisis con cProfile

La herramienta `cProfile` permitió identificar las funciones que consumían mayor tiempo de procesamiento.

Las funciones relacionadas con la validación de números primos fueron las más críticas en términos de rendimiento.

### Captura profiling

![Profiling](imagenes/imagen6.png)

## Comparación de tiempos de ejecución.
La gráfica muestra la diferencia entre el tiempo del código original y el código optimizado, evidenciando una mejora significativa en el rendimiento

![Codigo de creacion](imagenes/imagen9.png)

## Grafica comparativa

![Grafica](imagenes/grafica.png)

---

# Conclusiones

La optimización del código permitió reducir significativamente el tiempo de ejecución del programa.

El uso de raíz cuadrada, list comprehensions y arrays NumPy mejoró considerablemente el rendimiento del algoritmo.

La herramienta `cProfile` facilitó la detección de funciones críticas y el análisis del comportamiento del programa.

Finalmente, Git y GitHub permitieron gestionar correctamente el control de versiones del proyecto y facilitar la administración del código fuente.

![Imagen de commit de todos la carpetas](imagenes/imagen8.png)

---

# Repositorio GitHub

https://github.com/ALEX19877891/optimizacion-python