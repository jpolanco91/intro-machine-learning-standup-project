from MLUtility import MLUtility

util = MLUtility(['compression-ratio','engine-size'])

client_dictionary = {}
client_dictionary['symboling'] = 2
client_dictionary['normalized-losses'] = 170.0
client_dictionary['make'] = 'volvo'
client_dictionary['fuel-type'] = 'gas'
client_dictionary['aspiration'] = 'std'
client_dictionary['num-of-doors'] = 'four'
client_dictionary['body-style'] = 'sedan'
client_dictionary['drive-wheels'] = 'fwd'
client_dictionary['engine-location'] = 'front'
client_dictionary['wheel-base'] = 80.8
client_dictionary['length'] = 130.0
client_dictionary['width'] = 62.3
client_dictionary['height'] = 55.5
client_dictionary['curb-weight'] = 3000
client_dictionary['engine-type'] = 'dohc'
client_dictionary['num-of-cylinders'] = 'four'
client_dictionary['engine-size'] = 90
client_dictionary['fuel-system'] = 'mpfi'
client_dictionary['bore'] = 3.21
client_dictionary['stroke'] = 3.16
client_dictionary['compression-ratio'] = 8.09
client_dictionary['horsepower'] = 65
client_dictionary['peak-rpm'] = 4300
client_dictionary['city-mpg'] = 22
client_dictionary['highway-mpg'] = 30

# URI 1: ?symboling=2&normalized-losses=170.0&make=volvo&fuel-type=gas&aspiration=std&num-of-doors=four&body-style=sedan&drive-wheels=fwd&engine-location=front&wheel-base=80.8&length=130.0&width=62.3&height=55.5&curb-weight=3000&engine-type=dohc&num-of-cylinders=four&engine-size=90&fuel-system=mpfi&bore=3.21&stroke=3.16&compression-ratio=8.09&horsepower=65&peak-rpm=4300&city-mpg=22&highway-mpg=30
# URI 2: ?symboling=2&normalized-losses=188.0&make=bmw&fuel-type=gas&aspiration=std&num-of-doors=four&body-style=sedan&drive-wheels=fwd&engine-location=front&wheel-base=103.8&length=170.0&width=62.3&height=55.5&curb-weight=3000&engine-type=dohc&num-of-cylinders=four&engine-size=90&fuel-system=mpfi&bore=3.21&stroke=3.16&compression-ratio=8.09&horsepower=65&peak-rpm=4300&city-mpg=22&highway-mpg=30

print util.parse_features(client_dictionary)
