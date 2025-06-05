# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
#Importar librerias
import zipfile
import pandas as pd
import glob
import os

def pregunta_01():

    #Extraer datos
    path = "files/input.zip"
    destino = "files"
    with zipfile.ZipFile(path, 'r') as fzip:
        fzip.extractall(destino)

    def load_input(input_directory):
        secuence = []
        files = glob.glob(f"{input_directory}/**/*.txt", recursive=True)
        for file in files:
            with open(file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    label = os.path.basename(os.path.dirname(file))
                    secuence.append((line, label))
        return secuence

    #Creamos carpeta de salida
    def output_directory(output_directory):
        if os.path.exists(output_directory):
            for file in glob.glob(f"{output_directory}/*"):
                os.remove(file)
            os.rmdir(output_directory)
        os.makedirs(output_directory)
    

    #Guardamos en la carpeta de salida
    def save_output(output_directory, secuence):
        df = pd.DataFrame(secuence, columns=["phrase", "target"])
        df.to_csv(f"{output_directory}", index=False)    
    
    output_directory("files/output")
    
    train_data = load_input("files/input/train")
    test_data = load_input("files/input/test")
    
    save_output("files/output/train_dataset.csv", train_data)
    save_output("files/output/test_dataset.csv", test_data)

    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
pregunta_01()
