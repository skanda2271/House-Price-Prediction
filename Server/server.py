from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_locations_names')
def get_locations_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_price', methods =['POST'])
def predict_home_price():
    total_sqrft = float(request.form['total_sqrft'])
    location = (request.form['location'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqrft, bhk, bath)
    })
    return response

if __name__ == "__main__":
    util.load_artifacts()
    print("Hello")
    app.run(debug = True)