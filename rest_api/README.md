# Intro to Machine Learning standup (REST API)

Este es una REST API que utilizaremos para integrar el modelo ya creado (auto_recommender.pkl) dentro de un servicio web al cual le haremos request con datos de un vehiculo especifico para que nos devuelva un JSON con el precio recomendado.

# Requerimientos para el environment.

  - python 2.7.12
  - Flask
  - Flask RESTful

# Pasos para setear el environment.

1. Luego de haber clonado el repositorio, dentro de la carpeta ```intro-machine-learning-standup-project``` Cambiamos a la carpeta de rest_api con el comando ```cd rest_api```
2. Instalamos el framework Flask ejecutando ```pip install flask```
3. Instalamos Flask RESTful con el comando ```pip install flask_restful```
4. Ejecutamos la API con el comando ```python app.py```. La misma se estara ejecutando en la url http://localhost:5000.

# Haciendo requests a la API.

Este es el formato de url de un request a la API:

```http://localhost:5000/auto-price-recommender/api/recommend-price/?symboling=2&normalized-losses=170.0&make=volvo&fuel-type=gas&aspiration=std&num-of-doors=four&body-style=sedan&drive-wheels=fwd&engine-location=front&wheel-base=80.8&length=130.0&width=62.3&height=55.5&curb-weight=3000&engine-type=dohc&num-of-cylinders=four&engine-size=90&fuel-system=mpfi&bore=3.21&stroke=3.16&compression-ratio=8.09&horsepower=65&peak-rpm=4300&city-mpg=22&highway-mpg=30```

Solo tenemos que cambiar alguno de los parametros dentro del request para obtener alguna recomendacion diferente sobre el precio.


