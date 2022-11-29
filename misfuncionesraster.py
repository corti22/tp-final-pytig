#Curso: Programación en TIG con Python.

# TP FINAL
#- Fecha 29/11/2022
#- Alumno: Corti Marcelo 

#OBTENCION DE INFORMACION SOBRE INDICE NDWI

# Versiones utilizadas

#!python --version
#print ("La versión utilizada de numpy es:" , np.__version__)
#print ("La versión utilizada de rasterio es:" , rio.__version__)

#Python 3.9.13
#La versión utilizada de numpy es: 1.21.5
#La versión utilizada de rasterio es: 1.3.3

# Las bibliotecas de Python utilizadas fueron las siguientes:
# Para trabajar con estructura de datos que garantiza calculos con matrices y asi trabajar con arreglos de pixeles, se invoca:
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Para visualizar, manipular y crear datos raster, se invoca:
# La libreria rasterio permite la lectura, inspección y visualizacion de datos raster.
import rasterio as rio 
from rasterio.plot import show
from rasterio import plot
import os



# Se especifica la ruta de trabajo donde se encutran nuestras imágenes y metadatos:


#ruta_img="C:/Users/PC/Desktop/Landsat 8 -Octubre 2019/" (para caso de prueba)
#ruta_img=".../Landsat 8.../"

# Para leer los datos raster, se propone la siguiente funcion:
def Lectura (ruta_img):
    """Lee todas las bandas de una imagen LandSat 8 (ver el archivo de metadatos)
        ruta_img: recibe la ubicacion del directorio con el que se esta trabajando.
        Ej:nom_direc=f"C:/Users/PC/Desktop/Landsat 8 -Octubre 2019/
        Retorna el contenido ordenado de forma ascendente completo del archivo, mostrándolo en una lista donde cada elemento de la lista corresponde a una imágen del archivo"""
        
    list_bandas=os.listdir(ruta_img)
    list_bandas.sort(key=len,reverse=False)
    
    return(list_bandas)
    
##### Se invoca la siguiente funcion del modulo misfuncionesraster en el cuaderno de Jupyter-Lab
#lect=mfr.Lectura(ruta_img)
#lect

"""['LC08_L1TP_227081_20191012_20191018_01_T1_B1.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B2.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B3.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B4.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B5.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B6.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B7.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B8.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B9.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_ANG.txt',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B10.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_B11.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_BQA.TIF',
 'LC08_L1TP_227081_20191012_20191018_01_T1_MTL.txt']
"""

# Se procede a la apertura y análisis de datos raster.
#import rasterio as rio
#b3= rio.open(ruta_img+'LC08_L1TP_227081_20191012_20191018_01_T1_B3.TIF')
#b5= rio.open(ruta_img+'LC08_L1TP_227081_20191012_20191018_01_T1_B5.TIF')
#filas=b3.height
#filas=7891
#columnas=b3.width
#columnas=7831

def bandas (list_bandas):
     """Lee una lista de bandas ordenadas de una escena de LandSat 8
        list_bandas: re 
        Se tiene que volver a especificar el directorio. Ej:nom_direc=f"C:/Users/PC/Desktop/Landsat 8 -Octubre 2019/
        Convierte los valores de las imágenes de enteros a decimales para las bandas del verde y rojo
        Retorna un arreglo matricial (NDVI) con valores decimales entre -1 y 1 :"""
        
    import numpy as np
    import rasterio as rio
    imagenes = []
    ruta_img="C:/Users/PC/Desktop/Landsat 8 -Octubre 2019/"
    for banda in list_bandas:
        b3= rio.open(ruta_img+list_bandas[2])
        b5= rio.open(ruta_img+list_bandas[4])
        banda3=b3.read(1).astype('float64')
        banda5=b5.read(1).astype('float64')
        #imagenes=[banda3,banda5]
        nume= banda3-banda5
        deno= banda3+banda5
        np.seterr(divide = "ignore", invalid="ignore")
        ndwi = nume/deno
        ndwi[ndwi > 1] = np.nan
        ndwi[ndwi < -1] = np.nan
    return (ndwi)   
    #return (imagenes)


# Se clasifican los valores de numeros digitales para cada intervalo cada intervalo establecido

def contar_nd(img_ndwi):
    """Cuenta la cantidad de numeros digitales en imagen NDWI segun ciertas condicones
        img_ndwi: recibe una imagen LandaSat 8 con indice de influencia de agua normalizado (ndwi) con valores flotantes de -1 a 1.
        Retorna la superficie para cada condicion con la estructura {área,Ha}
    """
    m=7891
    n=7831
    cont_inund = 0 # Se inician contadores
    cont_humed = 0
    cont_seco = 0
    for f in range(m): # Se recorre la imágen por filas y columnas
        for c in range(n):            
            nd= img_ndwi[f,c] # Se obtiene el valor del numero digital para cada posición en la matriz                
            if  0.2<= nd<1:# si el valor del nd es mayor a 0.2 y menor a 1
                cont_inund = cont_inund + 1 # Cuento la cantidad de pixeles que cumplen esa condicion                                           
            elif 0<=nd<0.2:
                cont_humed = cont_humed + 1
            else:
                cont_seco = cont_seco + 1
    print("La superficie correspondiente al área inundada son : ", cont_inund*30*30/10000, "Ha")
    print("La superficie correspondiente el área humeda son : ", cont_humed*30*30/10000, "Ha")
    print("La superficie correspondiente al área seca son : ", cont_seco*30*30/10000, "Ha")       


#img_ndwi=ndwi_float
#sup_ndwi=mfr.contar_nd(img_ndwi)
