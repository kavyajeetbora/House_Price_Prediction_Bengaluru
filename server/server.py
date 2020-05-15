from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hey"

@app.route('/get_location_names')
def get_location_names():
    '''
    This function when called will create a response
    The response is to return all the location in bangalore city
    '''
    response = jsonify({
        'locations': util.get_location_names()
    })

    response.headers.add('Access-control-Allow-Origin','*')
    return response

@app.route('/predict_house_price',methods=['POST'])
def predict_house_price():
    '''
    This function calls the get_estimated_price function from util.py
    '''
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print('Starting Python Flask Server for House Price Prediction')
    util.load_saved_artifacts()
    app.debug = True
    app.run()
