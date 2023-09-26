# PEC 4

Para la realización de esta pec he creado una carpeta en la que se encuentran los archivos *main.py* (que contendrá las llamadas a las funciones principales), *func.py* (que contendrá las funciones), *test_func.py* (que contiene los test para los ejercicios 1.2 - 3), *requierements.txt* (que contiene la lista de librerías necesarias para ejecutar el código), *LICENSE.txt* (que contiene la licencia) y *setup.py*

Además para exportar el dataset y trabajar con el (a partir del ejercicio 4.2) se espera que haya una carpeta llamada "data" que contenga el archivo "twitter_processed.csv". Si no existe el código la creará y exportará el archivo en ella.

Para ejecutar el proyecto se puede abrir una terminal en la carpeta que contenga los archivos func.py y main.py y ejecutar el siguiente comando: python3 main.py. 

## Información general
Este paquete de pyton nos permite limpiar un dataset y resolver una serie de ejercicios propuestos con el objetivo de limpiar y organizar el dataset y analizar los datos que contiene. 

Cada función en func.py esta debidamente comentada, además si se desea reutilizar el código, se puede seguir como ejemplo el archivo main.py en el que se llama a las funciones definidas en func.py.   

Para resolver los ejercicios de una forma limpia he decidido crear una función para cada uno. A continuación detallo el nombre de la función de cada ejercicio y como llamarla. 

## Ejercicios:

### 1.1 
He descomprimido el archivo .zip de forma manual como se indicó en el foro de la asignatura

### 1.2 
La función que lee el fichero y carga el dataset como una lista de diccionarios es la función **cargar_dataset** definida en func y llamada en main. 

### 2.1 
La función que preprocesa el dataset y elimina las URLs, los caracteres especiales no ASCII y los símbolos y que convierte el texto a minúsculas es la función **preprocesar_dataset** definida en func y llamada en main. 

### 2.2 
La función que elimina las stopwords de los textos de los tuits es la función **eliminar_stopwords** definida en func y llamada en main.

### 3
La función que obtiene las frecuencias de las palabras de los textos de los tuits es la función **obtener_frecuencias** definida en func y llamada en main.

### 4.1
La función que completa el dataset añadiendo a cada registro una nueva variable con su diccionario de frecuencias de términos asociado es la función **completar_dataset_con_frecuencias** definida en func y llamada en main.

### 4.2
La función que guarda el dataset en un archivo CSV es la función **obtener_frecuencias** definida en func y llamada en main.

### 5
La función que genera un word cloud para cada cluster es la función **generar_word_clouds** definida en func y llamada en main.

### 6
La función que genera un histograma de las palabras más frecuentes para cada cluster es la función **generar_histograma** definida en func y llamada en main.

### 7
La función que devuelve los datos necesarios para responder a las preguntas sobre 
la frecuencia de palabras en críticas positivas y negativas es la función **preguntas_frecuencia_palabras** definida en func y llamada en main.

Si se ejecuta el archivo main.py desde la terminal de la carpeta se verán los resultados de cada uno (se puede utilizar el comando python3 main.py)

## Tests:

Para hacer los tests he creado un documento llamado *test_func.py*. 

Para ejecutarlos con Coverage.py hay que ejecutar el siguiente comando el la terminal: coverage run -m unittest test_func.py

Esto generará un informe de cobertura que se puede ver ejecutando: coverage report

### Primer test: (ej 1.2)
En el primer test verificamos que el dataset no está vacío, que el primer elemento del dataset es un diccionario y que el diccionario tiene las claves correctas. 

### Segundo test: (ej 2.1)
En el segundo test introducimos un dataset de prueba y comprobamos que la función devuelve el resultado que debería. 

- Si introducimos: @switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer. You shoulda got David Carr of Third Day to do it. ;D
- Deberíamos obtener: switchfoot awww that s a bummer you shoulda got david carr of third day to do it d

### Tercer test: (ej 2.2)
En el tercer test introducimos un dataset de prueba con el resultado que daría la función eliminar_stopwords y comprobamos que la función devuelve el resultado que debería. 

- Si introducimos: switchfoot awww that s a bummer you shoulda got david carr of third day to do it d
- Deberíamos obtener: switchfoot awww bummer shoulda got david carr third day d

### Cuarto test: (ej 3)
En el cuarto test introducimos un dataset de prueba con el resultado que daría la función obtener_frecuencias y comprobamos que la función devuelve el resultado que debería. 

- Si introducimos: switchfoot awww bummer shoulda got david carr third day d
- Deberíamos obtener: 
{
    'switchfoot':1,
    'awww': 1,
    'bummer': 1,
    'shoulda':1,
    'got': 1,
    'david': 1,
    'carr': 1,
    'third': 1,
    'day': 1, 
    'd':1
}

### Quinto test: (ej 4.1)
De la misma forma que en el cuarto test, introducimos un dataset de brueba con el resultado que daría la función completar_dataset_con_frecuencias y comprobamos que la función devuelve el resultado que debería. 

- Si introducimos: switchfoot awww bummer shoulda got david carr third day d
- Deberíamos obtener: 
{
    'switchfoot':1,
    'awww': 1,
    'bummer': 1,
    'shoulda':1,
    'got': 1,
    'david': 1,
    'carr': 1,
    'third': 1,
    'day': 1, 
    'd':1
}

### Sexto y séptimo test: (ej 5 y 6)
Tal y como se indicó en el tablón de la asignatura estos tests comprueban que se produzcan excepciones con las entradas no válidas y las entradas incorrectas. 

**Estos tests proporcionan la siguiente cobertura:**

Name           Stmts   Miss  Cover
----------------------------------
func.py          119     58    51%
test_func.py      68      0   100%
----------------------------------
TOTAL            187     58    69%


## Requeriments: 

El archivo requeriments.txt contiene las librerías necesarias para ejecutar el código. 
Estas librerías se pueden instalar utilizando el comando: pip install -r requirements.txt

## setup.py 

Este archivo instalará las dependencias automaticamente, para ejecutar el archivo se puede utilizar el siguiente comando: python3 setup.py install