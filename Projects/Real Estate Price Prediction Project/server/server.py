from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'GET' or request.method == 'POST':
        # Use request.args for query parameters or fallback to form data
        total_sqft = float(request.args.get('total_sqft') or request.form.get('total_sqft'))
        location = request.args.get('location') or request.form.get('location')
        bhk = int(request.args.get('bhk') or request.form.get('bhk'))
        bath = int(request.args.get('bath') or request.form.get('bath'))

        response = jsonify({
            'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()