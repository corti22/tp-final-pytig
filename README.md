Curso: Programación en TIG con Python.

TP FINAL
- Fecha 29/11/2022
- Alumno: Corti Marcelo 

OBTENCION DE INFORMACION SOBRE INDICE NDWI

Problema: Extraer informacion de clases de acuerdo a umbrales sobre una imágen satelital óptica Landsat 8 con Índice de agua de Diferencia Normalizado (NDWI) empleando algoritmos en lenguaje Python.

Tiene como objetivo la identificación aproximada de la variacion de los cauces de rios y lagunas bajo condiciones extremas.

Para leer los datos raster, se importa:
Se especifica la ruta de trabajo donde se encutran nuestras imágenes y metadatos:

Ejemplo: ruta_img=".../Landsat 8.../"


Nota: Se propone trabajar con escenas completas, es decir, con las metadatos de descarga. La secuencia de estos subprogramas, se deben replicar para cada escena. 
Observación: Para este trabajo tambien se probo con la imágen de 18 de Octubre del 2019 zona Sunchales path-row=227081 (vista en clases). De modo que se puedan correr los subprogramas sin necesidad de descargar las escenas propuestas"""
Aclariacion: No se utilizarion recortes (sub-escenas). 

