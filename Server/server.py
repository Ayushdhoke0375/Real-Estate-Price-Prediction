import flask
import util
from waitress import serve

app = flask.Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = flask.jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(flask.request.form['total_sqft'])
    location = flask.request.form['location']
    bhk = int(flask.request.form['bhk'])
    bath = int(flask.request.form['bath'])

    response = flask.jsonify({
        'estimated_price': util.get_estimated_price(total_sqft, bhk, bath, location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting python flask server for home price prediction...")
    util.load_saved_artifacts()
    serve(app, host='0.0.0.0', port=5000, threads=2)
