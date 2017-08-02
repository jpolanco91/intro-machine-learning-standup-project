# Intro to Machine Learning standup.

Este es el proyecto relacionado con el standup de Machine Learning presentado en Intellisys D. Corp. donde el proyecto consiste en utilizar un dataset, de automoviles para construir un sistema de recomendacion en el cual dados los parametros (atributos) de un automovil este nos recomiende el precio al cual debemos de venderlo.

El proyecto incluye tambien una REST API donde veremos como integrar el modelo con una aplicacion web para que la misma haga recomendaciones de los precios de los automoviles.

# Requerimientos para el environment.

  - python 2.7.12
  - Anaconda 4.2.0

# Pasos para setear el environment.

1. Descargar e instalar la distribucion de Data Science Anaconda (https://www.continuum.io), la version para Python 2.7
  * Pasos instalacion Windows: https://docs.continuum.io/anaconda/install/windows
  * Pasos instalacion macOS: https://docs.continuum.io/anaconda/install/mac-os
  * Pasos instalacion Linux: https://docs.continuum.io/anaconda/install/linux
2. Luego clonar este repositorio usando ```git clone https://github.com/jpolanco91/intro-machine-learning-standup-project.git``` luego cambiar al directorio generado por el repositorio (intro-machine-learning-standup-project).
3. Ejecutar el comando ```jupyter notebook precios_automovil.ipynb``` y esto comenzara a correr un servidor web en el puerto 8888 que cargara el notebook con el codigo del proyecto. Accedemos a el usando el navegador mediante la url http://localhost:8888. Luego veremos que hay una lista de archivos y hacemos clic en el que dice precios_automovil.ipynb y ahi comenzara el programa.
4. Para ejecutar el codigo solo debemos colocarnos en una celda donde hay codigo y darle clic al boton run cell.
