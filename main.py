# IMPORTO LAS FUNCIONES
from func import cargar_dataset  # ej 1.2
from func import preprocesar_dataset  # ej 2.1
from func import eliminar_stopwords  # ej 2.2
from func import obtener_frecuencias  # ej 3
from func import completar_dataset_con_frecuencias  # ej 4.1
from func import guardar_dataset_csv  # ej 4.2
from func import generar_word_clouds  # ej 5.3
from func import generar_histograma  # ej 6
from func import preguntas_frecuencia_palabras  # ej 7

import pandas as pd  # leer el csv que hemos creado en ej 4


# Ruta del archivo "twitter_reduced.csv"
file_path = "data/twitter_reduced.csv"

# Ejercicio 1.2:
print("\n🥭 Ejercicio 1.2:\n lectura del fichero y carga del dataset como una lista de diccionarios:\n")
# Llamada a la función cargar_dataset
dataset = cargar_dataset(file_path)
# Imprimir los 5 primeros registros del dataset
print("5 primeros registros del dataset:\n")
for i in range(5):
    print(dataset[i])

# Ejercicio 2.1
print("\n🥭 Ejercicio 2.1:\n preprocesado del texto: \n")
# Llamada a la función preprocesar_dataset
dataset_preprocesado = preprocesar_dataset(dataset)

# Ejercicio 2.2
print("\n🥭 Ejercicio 2.2: eliminamos las stopwords: \n")
# Llamada a la función eliminar_stopwords
dataset_sin_stopwords = eliminar_stopwords(dataset_preprocesado)
# Imprimir las 5 últimas filas
ultimas_filas = dataset_sin_stopwords[-5:]
for tweet in ultimas_filas:
    print(tweet)


# Ejercicio 3
print("\n🥭 Ejercicio 3:\n obtenemos la frecuencia de las palabras en el texto:\n")
# Llamada a la función eliminar_stopwords
frecuencias, vocabulario = obtener_frecuencias(dataset_sin_stopwords)
# 5 primeros elementos de la lista de diccionarios
print(frecuencias[:5])
# 10 primeras palabras del vocabulario ordenado alfabéticamente
vocabulario_ordenado = sorted(list(vocabulario))
print(vocabulario_ordenado[:10])


# Ejercicio 4.1
print("\n🥭 Ejercicio 4.1:\n añadimos una nueva variable al dataset con la frecuencia:\n")
# Llamada a la función completar_dataset_con_frecuencias
completar_dataset_con_frecuencias(dataset)
# Imprimir elemento 20 del dataset
print("Elemento 20 del dataset:", dataset[19])


# Ejercicio 4.2
print("\n🥭 Ejercicio 4.2:\n guardamos el dataset en formato csv\n")
# Llamada a la función guardar_dataset_csv
guardar_dataset_csv(dataset, "twitter_processed.csv")


# leemos el csv
df = pd.read_csv("data/twitter_processed.csv")

# Ejercicio 5
print("\n🥭 Ejercicio 5:\n")
# ¿Cuántos clusters tenemos en nuestro dataset?
num_clusters = len(df['sentiment'].unique())
print("Número de clusters en el dataset:", num_clusters)

# ¿Tenemos elementos vacíos en las columnas text? ¿Si es así, cuál es el porcentaje?
porcentaje_null = df['text'].isnull().sum() / len(df) * 100
print("Porcentaje de elementos nulos en la columna 'text':", porcentaje_null, "%")
# Eliminar los elementos nulos antes de generar el word cloud
df = df.dropna(subset=['text'])

# Generar un word cloud para cada cluster.
# Llamada a la función generar_word_clouds
print("Generamos word cloud para cada cluster")
generar_word_clouds(df)


# Ejercicio 6
print("\n🥭 Ejercicio 6:\n Generamos un histograma con las palabras de cada cluster\n")
# Llamada a la función generar_histogramas
generar_histograma(df, 20)


# Ejercicio 7
print("\n🥭 Ejercicio 6:\n")
num = 5
positivas, negativas, comunes = preguntas_frecuencia_palabras(df, num)

print(f"{num} palabras más utilizadas en las críticas positivas:")
for palabra, frecuencia in positivas:
    print(palabra, "-", frecuencia)

print(f"\n{num} palabras más utilizadas en las críticas negativas:")
for palabra, frecuencia in negativas:
    print(palabra, "-", frecuencia)

print(f"\n{num} palabras comunes en las críticas positivas y negativas:")
print(comunes)

print("A partir de la word cloud, ¿qué se puede deducir sobre el sentimiento general de cada grupo?\n Como podemos observar, las personas de los comentarios del cluster 4 expresan felicidad mediante palabras como love, thank, great, nice, amazing...\n Por otra parte las personas de los comentarios del cluster 0 expresan tristeza mediante plabras como miss, hate, sorry, suck, tired... ")
