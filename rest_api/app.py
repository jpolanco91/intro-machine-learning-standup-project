from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from MLUtility import MLUtility
import pickle
import os

# Inicializando el web service.
app = Flask(__name__)
api = Api(app)

#Inicializando el modelo.
reg = pickle.load(open('auto_recommender.pkl', 'rb'))

class PrecioAutoRecommenderHandler(Resource):

    def get(self):
        # Transformamos en diccionario los datos obtenidos del usuario
        auto_data = {}
        auto_data['symboling'] = int(request.args.get('symboling'))
        auto_data['normalized-losses'] = float(request.args.get('normalized-losses'))
        auto_data['make'] = request.args.get('make')
        auto_data['fuel-type'] = request.args.get('fuel-type')
        auto_data['aspiration'] = request.args.get('aspiration')
        auto_data['num-of-doors'] = request.args.get('num-of-doors')
        auto_data['body-style'] = request.args.get('body-style')
        auto_data['drive-wheels'] = request.args.get('drive-wheels')
        auto_data['engine-location'] = request.args.get('engine-location')
        auto_data['wheel-base'] = float(request.args.get('wheel-base'))
        auto_data['length'] = float(request.args.get('length'))
        auto_data['width'] = float(request.args.get('width'))
        auto_data['height'] = float(request.args.get('height'))
        auto_data['curb-weight'] = float(request.args.get('curb-weight'))
        auto_data['engine-type'] = request.args.get('engine-type')
        auto_data['num-of-cylinders'] = request.args.get('num-of-cylinders')
        auto_data['engine-size'] = float(request.args.get('engine-size'))
        auto_data['fuel-system'] = request.args.get('fuel-system')
        auto_data['bore'] = float(request.args.get('bore'))
        auto_data['stroke'] = float(request.args.get('stroke'))
        auto_data['compression-ratio'] = float(request.args.get('compression-ratio'))
        auto_data['horsepower'] = float(request.args.get('horsepower'))
        auto_data['peak-rpm'] = float(request.args.get('peak-rpm'))
        auto_data['city-mpg'] = float(request.args.get('city-mpg'))
        auto_data['highway-mpg'] = float(request.args.get('highway-mpg'))

        # Creamos un objeto de MLUtility para los helper de parseo. Insertamos
        # los atributos altamente sesgados para fines de transformacion de los
        # datos.
        ml_util = MLUtility(['compression-ratio','engine-size'])

        # Parseamos la data al formato que acepta el modelo de ML.
        parsed_features = ml_util.parse_features(auto_data)

        # Le pasamos la data transformada al modelo para realizar la prediccion.
        price = reg.predict(parsed_features)[0]

        # Preparamos la respuesta en un diccionario para llevarla a JSON.
        response = {}
        response['precio'] = price

        return jsonify(response)


# Endpoint para generar recomendacion.
api.add_resource(PrecioAutoRecommenderHandler, '/auto-price-recommender/api/recommend-price/')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
