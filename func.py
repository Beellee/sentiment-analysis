# imports
import pandas as pd
import csv
import re
from collections import Counter
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# 1.2
def cargar_dataset(file_path: str):

    """
        Carga un dataset desde un archivo CSV como una lista de diccionarios.
        Args:
            file_path (str): Ruta del archivo CSV a cargar.
        Returns:
            list: Lista de diccionarios que representan las filas del dataset.
    """
    dataset = []

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dataset.append(row)

    return dataset


# 2.1
def preprocesar_dataset(dataset: list):

    """
        Realiza el preprocesamiento de texto en un dataset dado.
        Args:
            dataset (list): Lista de diccionarios que representan las filas del dataset.
        Returns:
            list: El dataset preprocesado con los textos modificados.
    """
    for tweet in dataset:
        text = tweet['text']
        # Eliminamos las URLs
        text = re.sub(r'http\S+', '', text)
        # Eliminamos caracteres especiales, símbolos y números
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)
        # Convertimos el texto a minúsculas
        text = text.lower()
        # Reemplazamos los espacios en blanco múltiples por uno solo
        text = re.sub(r'\s+', ' ', text)
        # Eliminamos los espacios en blanco al inicio y al final del texto
        text = text.strip()
        # Reemplazamos el texto original por el texto preprocesado en el dataset
        tweet['text'] = text

    return dataset


# 2.2
def eliminar_stopwords(dataset: list):

    """
        Elimina las stopwords de los textos en un dataset dado.
        Args:
            dataset (list): Lista de diccionarios que representan las filas del dataset.
        Returns:
            list: El dataset con los textos modificados, sin las stopwords.
    """
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

    for tweet in dataset:
        text = tweet['text']
        # Dividimos el texto en palabras individuales
        words = text.split()
        # Eliminamos las stopwords de las palabras
        words = [word for word in words if word not in stopwords]
        # Unimos las palabras nuevamente en un texto
        text_without_stopwords = ' '.join(words)
        # Reemplazamos el texto original por el texto sin stopwords en el dataset
        tweet['text'] = text_without_stopwords

    return dataset


# 3
def obtener_frecuencias(dataset: list):

    """
        Obtiene las frecuencias de palabras en un dataset y el vocabulario único.
        Args:
            dataset (list): Lista de diccionarios que representan las filas del dataset.
        Returns:
            tuple: Una tupla que contiene dos elementos:
                - frecuencias (list): Lista de diccionarios que representan las frecuencias de palabras en cada tuit del dataset.
                - vocabulario (set): Conjunto de palabras únicas presentes en el dataset.
    """

    frecuencias = []  # Palabras y su frecuencia
    vocabulario = set()  # Palabras únicas

    for tuit in dataset:

        palabras = tuit['text'].split()  # Obtenemos las palabras del tuit actual

        contador = {}  # Diccionario con las frecuencias de palabras del tuit

        for palabra in palabras:
            if palabra not in contador:
                contador[palabra] = 0  # Inicializamos la frecuencia de la palabra en 0
            contador[palabra] += 1  # Actualizamos la frecuencia de la palabra

            vocabulario.add(palabra)  # Agregamos la palabra al vocabulario
        frecuencias.append(contador)  # Agregamos el diccionario de frecuencias a la lista
    return frecuencias, vocabulario


# 4.1
def completar_dataset_con_frecuencias(dataset: list):

    """
        Completa el dataset con las frecuencias de términos para cada registro.
        Args:
            dataset (list): Lista de diccionarios que representan las filas del dataset.
        Returns:
            None: (la función no devuelve ningún valor si no que modifica el dataset directamente)
    """

    frecuencias, _ = obtener_frecuencias(dataset)  # Obtenemos las frecuencias de términos y el vocabulario (pero como el vocabulario no nos sirve de nada utilizamos "_")

    for i, registro in enumerate(dataset):
        registro['frequencies'] = frecuencias[i]


# 4.2
def guardar_dataset_csv(dataset: list, nombre_archivo: str):

    """
        Guarda un dataset en un archivo CSV.
        Args:
            dataset (list): Lista de diccionarios que representan las filas del dataset.
            nombre_archivo (str): Nombre del archivo CSV a guardar.
        Returns:
            None: (la función no devuelve ningún valor si no que guarda guarda el dataset en un archivo CSV)
    """

    ruta_archivo = "data/" + nombre_archivo  # Ruta del archivo CSV
    # Establecemos los campos del dataset
    campos = ['sentiment', 'id', 'date', 'query', 'user', 'text', 'frequencies']

    ruta_archivo = os.path.join("data/", nombre_archivo)  # Ruta del archivo CSV

    # Para la ejecución del ejercicio no sería necesario imprimir si existe o no la carpeta y el archivo pero considero que aporta claridad.
    # Comprobar si la carpeta 'data' existe, y crearla si es necesario
    if not os.path.exists("data"):
        print("la carpeta data no existe, creando una nueva carpeta...")
        os.makedirs("data")

    # Ver si el archivo existe
    if os.path.exists(ruta_archivo):
        print(f"El archivo '{nombre_archivo}' ya existe, se sobreescribirán los datos.")
    else:
        print(f"El archivo'{nombre_archivo}' no existe, creando uno y añadiendo datos...")

    # crear o sobreescribir el archivo
    with open(ruta_archivo, 'w') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)

        writer.writeheader()  # línea de encabezado

        # cada registro del dataset
        for registro in dataset:
            writer.writerow(registro)


# 5 apartado 3
def generar_word_clouds(dataset: pd.DataFrame):

    """
        Genera un word cloud para cada cluster.
        Args:
            dataset (DataFrame): Dataset que contiene los textos y los clusters de cada registro.
        Raises:
            ValueError: Si el dataset está vacío.
            KeyError: Si falta la columna 'sentiment' en el dataset.
        Returns:
            None
    """
    if dataset.shape[0] == 0:
        raise ValueError("El dataset está vacío.")

    if 'sentiment' not in dataset.columns:
        raise KeyError("Falta la columna 'sentiment' en el dataset.")

    # Agrupamos los datos por 'sentiment' y combinamos los textos correspondientes
    grouped_data = dataset.groupby('sentiment')['text'].apply(lambda x: ' '.join(x))

    for sentiment, text in grouped_data.items():
        count = len(dataset[dataset['sentiment'] == sentiment])
        print(f"Número de elementos en el cluster {sentiment}: {count}")

    # Generamos un word cloud para cada cluster
    for sentiment, text in grouped_data.items():
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title(f"Word Cloud - Cluster {sentiment}")
        plt.axis('off')
        plt.show()


# 6
def generar_histograma(dataset: pd.DataFrame, num: int):

    """
        Genera un histograma de las palabras más frecuentes para cada cluster.
        Args:
            dataset (DataFrame): Dataset que contiene los textos y los clusters de cada registro.
            num (int): Número de palabras más frecuentes a mostrar en el histograma.
        Raises:
            ValueError: Si el dataset no es un DataFrame o no contiene las columnas requeridas.
            ValueError: Si el número de palabras solicitado es menor o igual a cero.
        Returns:
            None: (simplemente genera los histogramas)
    """
    if not isinstance(dataset, pd.DataFrame):
        raise ValueError("El dataset debe ser un DataFrame")

    required_columns = ['sentiment', 'text']
    if not all(col in dataset.columns for col in required_columns):
        raise ValueError("El dataset debe contener las columnas 'sentiment' y 'text'")

    if num <= 0:
        raise ValueError("El número de palabras debe ser mayor que cero")

    # Obtenemos los clusters únicos en el dataset
    clusters = dataset['sentiment'].unique()
    # Para cada cluster:
    for cluster in clusters:
        # Filtramos el dataset por el cluster actual
        cluster_data = dataset[dataset['sentiment'] == cluster]
        # Unimos los textos de los tweets en un solo string
        text = ' '.join(cluster_data['text'])
        # Tokenizamos el string en palabras individuales
        palabras = text.split()
        # Calculamos la frecuencia de cada palabra
        frecuencias = Counter(palabras)
        # Obtenemos las num palabras con mayor frecuencia
        top_palabras = frecuencias.most_common(num)
        # Separamos las palabras y sus frecuencias en listas separadas
        palabras, valores = zip(*top_palabras)
        # Generamos el histograma
        plt.figure()
        plt.bar(palabras, valores)
        plt.title(f"{num} palabras más frecuentes - Cluster {cluster}")
        plt.xlabel('Palabras')
        plt.ylabel('Frecuencia')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()


# 7
def preguntas_frecuencia_palabras(dataset: pd.DataFrame, num: int):

    """
        Devuelve los datos necesarios para responder a las preguntas sobre
        la frecuencia de palabras en críticas positivas y negativas.
        Args:
            dataset (DataFrame): Dataset que contiene los textos y los clusters de cada registro.
            num (int): Número de palabras más utilizadas a obtener.
        Returns:
            tuple: Una tupla que contiene tres listas: palabras más utilizadas en críticas positivas,
                palabras más utilizadas en críticas negativas y palabras comunes entre ambas.
    """
    # Filtrar el dataset por críticas positivas y negativas
    criticas_positivas = dataset[dataset['sentiment'] == 4]
    criticas_negativas = dataset[dataset['sentiment'] == 0]

    # Unir los textos de las críticas positivas y negativas en un solo string
    texto_positivo = ' '.join(criticas_positivas['text'])
    texto_negativo = ' '.join(criticas_negativas['text'])

    # Tokenizar el texto de las críticas positivas y obtener las palabras más utilizadas
    palabras_positivas = texto_positivo.split()
    frecuencias_positivas = Counter(palabras_positivas)
    palabras_mas_utilizadas_positivas = frecuencias_positivas.most_common(num)

    # Tokenizar el texto de las críticas negativas y obtener las palabras más utilizadas
    palabras_negativas = texto_negativo.split()
    frecuencias_negativas = Counter(palabras_negativas)
    palabras_mas_utilizadas_negativas = frecuencias_negativas.most_common(num)

    # Obtener las palabras comunes entre las críticas positivas y negativas
    palabras_comunes = set(palabras_positivas) & set(palabras_negativas)
    palabras_comunes = list(palabras_comunes)[:num]

    return palabras_mas_utilizadas_positivas, palabras_mas_utilizadas_negativas, palabras_comunes
