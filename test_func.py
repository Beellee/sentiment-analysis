import unittest
from func import cargar_dataset
from func import preprocesar_dataset
from func import eliminar_stopwords
from func import obtener_frecuencias
from func import completar_dataset_con_frecuencias
import pandas as pd
from func import generar_histograma
from func import generar_word_clouds


# test para el ej 1.2
class TestCargarDataset(unittest.TestCase):

    def test_cargar_dataset(self):
        dataset = cargar_dataset("data/twitter_reduced.csv")

        # Verificamos que el dataset no está vacío
        self.assertNotEqual(len(dataset), 0)

        # Verificamos que el primer elemento del dataset es un diccionario
        self.assertIsInstance(dataset[0], dict)

        # Verificamos que el diccionario tiene las claves correctas
        expected_keys = ['sentiment', 'id', 'date', 'query', 'user', 'text']
        self.assertCountEqual(list(dataset[0].keys()), expected_keys)


# test para el ej 2.1
class TestPreprocesarDataset(unittest.TestCase):

    def test_preprocesar_dataset(self):

        # Dataset de prueba:
        dataset = [
            {
                'sentiment': '0',
                'id': '1467810369',
                'date': 'Mon Apr 06 22:19:45 PDT 2009',
                'query': 'NO_QUERY',
                'user': 'TheSpecialOne',
                'text': "@switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer. You shoulda got David Carr of Third Day to do it. ;D"
            }
        ]

        dataset_preprocesado = preprocesar_dataset(dataset)

        # Verificamos que el dataset preprocesado no está vacío
        self.assertNotEqual(len(dataset_preprocesado), 0)

        # Verificamos que el primer elemento del dataset preprocesado coincide con cómo debería ser
        expected_text = "switchfoot awww that s a bummer you shoulda got david carr of third day to do it d"
        self.assertEqual(dataset_preprocesado[0]['text'], expected_text)


# test para el ej 2.2
class TestEliminarStopwords(unittest.TestCase):

    # Introducimos un dataset de prueba con el resultado que daría la función preprocesar_dataset
    def test_eliminar_stopwords(self):
        dataset = [
            {
                'sentiment': '0',
                'id': '1467810369',
                'date': 'Mon Apr 06 22:19:45 PDT 2009',
                'query': 'NO_QUERY',
                'user': 'TheSpecialOne',
                'text': "switchfoot awww that s a bummer you shoulda got david carr of third day to do it d"
            }
        ]

        dataset_sin_stopwords = eliminar_stopwords(dataset)

        # Verificamos que el dataset sin stopwords no está vacío
        self.assertNotEqual(len(dataset_sin_stopwords), 0)

        # Verificamos que el primer elemento del dataset sin stopwords coincide con como debería ser
        expected_text = "switchfoot awww bummer shoulda got david carr third day d"
        self.assertEqual(dataset_sin_stopwords[0]['text'], expected_text)


# test para el ej 3
class TestObtenerFrecuencias(unittest.TestCase):

    # Introducimos un dataset de prueba con el resultado que daría la función eliminar_stopwords
    def test_obtener_frecuencias(self):
        dataset = [
            {
                'sentiment': '0',
                'id': '1467810369',
                'date': 'Mon Apr 06 22:19:45 PDT 2009',
                'query': 'NO_QUERY',
                'user': 'TheSpecialOne',
                'text': "switchfoot awww bummer shoulda got david carr third day d"
            }
        ]

        frecuencias, vocabulario = obtener_frecuencias(dataset)

        # Verificamos que las frecuencias no están vacías
        self.assertNotEqual(len(frecuencias), 0)

        # Verificar que el primer elemento de las frecuencias tiene la estructura correcta
        expected_frequencies = {
            'switchfoot': 1,
            'awww': 1,
            'bummer': 1,
            'shoulda': 1,
            'got': 1,
            'david': 1,
            'carr': 1,
            'third': 1,
            'day': 1,
            'd': 1
        }
        self.assertDictEqual(frecuencias[0], expected_frequencies)

        # Verificamos que el vocabulario no está vacío
        self.assertNotEqual(len(vocabulario), 0)

        # Verificamos que todas las palabras del primer tuit están presentes en el vocabulario
        words = dataset[0]['text'].split()
        for word in words:
            self.assertIn(word, vocabulario)


# test para el ej 4.1
class TestCompletarDatasetConFrecuencias(unittest.TestCase):

    def test_completar_dataset_con_frecuencias(self):
        dataset = [
            {
                'sentiment': '0',
                'id': '1467810369',
                'date': 'Mon Apr 06 22:19:45 PDT 2009',
                'query': 'NO_QUERY',
                'user': 'TheSpecialOne',
                'text': "switchfoot awww bummer shoulda got david carr third day d"
            }
        ]

        completar_dataset_con_frecuencias(dataset)

        # Verificamos que la nueva variable 'frequencies' está presente en cada registro del dataset
        for registro in dataset:
            self.assertIn('frequencies', registro)

        # Verificamos que las frecuencias del primer registro coinciden con las obtenidas previamente
        expected_frequencies = {
            'switchfoot': 1,
            'awww': 1,
            'bummer': 1,
            'shoulda': 1,
            'got': 1,
            'david': 1,
            'carr': 1,
            'third': 1,
            'day': 1,
            'd': 1
        }
        self.assertDictEqual(dataset[0]['frequencies'], expected_frequencies)


# test para el ej 5.3 (wordcloud)
class TestGenerarWordClouds(unittest.TestCase):

    def test_entrada_no_valida(self):
        # Probar con dataset vacío
        dataset = pd.DataFrame(columns=['sentiment', 'text'])
        with self.assertRaises(ValueError):
            generar_word_clouds(dataset)

    def test_entrada_incorrecta(self):
        # Probar con dataset que falta la columna 'sentiment'
        dataset = pd.DataFrame(columns=['text'])
        self.assertRaises(ValueError, lambda: generar_word_clouds(dataset))


# test para el ej 6 (histograma)
class TestGenerarHistograma(unittest.TestCase):

    def test_entrada_no_valida(self):
        dataset = "no es un DataFrame válido"
        num = 5
        with self.assertRaises(ValueError):
            generar_histograma(dataset, num)

    def test_entrada_incorrecta(self):
        # Probar la función con un dataset que no contiene las columnas requeridas
        dataset = pd.DataFrame({'label': [0, 1, 0], 'message': ['Hola', 'Mundo', 'Hola Mundo']})
        num = 5

        # Verificar que la función lanza una excepción
        with self.assertRaises(ValueError):
            generar_histograma(dataset, num)
