# Import necessary libraries
from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

# Load the models
log_model = joblib.load("backend/models/logistic_model.pkl")
rf_model = joblib.load("backend/models/random_forest_model.pkl")
scaler = joblib.load("backend/models/scaler.pkl")

# Crop emoji mapping
crop_emojis = {
    'rice': '🌾',
    'maize': '🌽',
    'chickpea': '🧆',
    'kidneybeans': '🫘',
    'pigeonpeas': '🌿',
    'mothbeans': '🌱',
    'mungbean': '🌱',
    'blackgram': '🌰',
    'lentil': '🥣',
    'pomegranete': '🍎',
    'banana': '🍌',
    'mango': '🥭',
    'grpaes': '🍇',
    'watermelom': '🍉',  
    'apple': '🍎',
    'orange': '🍊',
    'papaya': '🍈',
    'coconut': '🥥',
    'cotton': '🧵',
    'jute': '🪢',
    'coffee': '☕'
}


@app.route('/predict', methods=['POST'])
def predict():
    # Get User data from Frontend
    data = request.get_json()
    N = float(data['N'])
    P = float(data['P'])
    K = float(data['K'])
    ph = float(data['ph'])
    model_choice = data['model']

    input_data = pd.DataFrame([[N, P, K, ph]], columns=['N', 'P', 'K', 'ph'])

    # Predict the Crop
    if model_choice == 'logistic':
        input_scaled = scaler.transform(input_data)
        prediction = log_model.predict(input_scaled)[0]
    elif model_choice == 'rf':
        prediction = rf_model.predict(input_data)[0]
    else:
        return jsonify({'error': 'Invalid model selected'}), 400

    emoji = crop_emojis.get(prediction.lower())
    return jsonify({'crop': prediction, 'emoji': emoji})

if __name__ == '__main__':
    app.run(debug=True)
