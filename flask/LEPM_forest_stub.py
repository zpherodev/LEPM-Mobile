# LEPM_forest_stub.py
# Stub for integrating smartphone magnetic data with server-side forest model

from flask import Flask, request, jsonify
import joblib
import numpy as np
import datetime

app = Flask(__name__)

# Load pre-trained forest model
model = joblib.load('magnetic_forest_model.pkl')  # Must match your trained model file

@app.route('/submitMagnetometerData', methods=['POST'])
def submit_data():
    data = request.get_json()

    try:
        # Extract data from JSON
        bx = data['bx']   # microtesla, X axis
        by = data['by']   # microtesla, Y axis
        bz = data['bz']   # microtesla, Z axis
        lat = data['lat']
        lon = data['lon']
        timestamp = data.get('timestamp', str(datetime.datetime.utcnow()))

        # Compute derived features
        magnitude = np.sqrt(bx**2 + by**2 + bz**2)
        declination = np.arctan2(by, bx)
        inclination = np.arctan2(bz, np.sqrt(bx**2 + by**2))

        # Create feature vector (adjust to match your model’s expectations)
        X = np.array([[declination, inclination, magnitude]])

        # Predict with forest model
        prediction = model.predict(X)[0]  # e.g., 0 = Stable, 1 = Event
        confidence = max(model.predict_proba(X)[0])

        return jsonify({
            'prediction': int(prediction),
            'confidence': round(float(confidence), 4),
            'timestamp': timestamp,
            'location': {'lat': lat, 'lon': lon},
            'declination': round(float(declination), 4),
            'inclination': round(float(inclination), 4),
            'magnitude': round(float(magnitude), 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
