from setuptools import setup

setup(
    name='analisis_de_sentimientos_Twitter',
    version='1.0.0',
    author='Paula Corbatón Álvarez',
    author_email='paula-alvarez@uoc.edu',
    description='Paquete para realizar análisis de sentimientos en texto',
    packages=['analisis_de_sentimientos_Twitter'],
    install_requires=[
        'pandas',
        'matplotlib',
        'wordcloud',
        're',
        'collections',
        'os'
    ]
)
