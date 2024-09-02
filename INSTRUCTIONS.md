
# Instructions for Using the Earthquake Prediction Model

## Overview
This guide provides instructions on how to use the trained Random Forest model for earthquake prediction using magnetic field data from the EMAG2 dataset or similar datasets. The model predicts the likelihood of an earthquake occurring based on magnetic anomalies detected in the data.

## Prerequisites
- Python 3.x installed
- Required Python libraries: `pandas`, `numpy`, `scikit-learn`, `pickle`
- Magnetic field data (e.g., from the EMAG2 dataset)

## Step-by-Step Instructions

### 1. Clone the Repository and Load the Model
Clone the Git repository containing the model and supporting files:

```bash
git clone <your-git-repo-url>
cd <your-git-repo-directory>
```

Load the model using Python:

```python
import pickle

# Load the Random Forest model
with open('earthquake_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)
```

### 2. Prepare the EMAG2 Data
Ensure your magnetic field data (e.g., from the EMAG2 dataset) is formatted correctly. The data should include the following features:
- `decg`: Declination in degrees
- `dbhg`: Horizontal field component
- `decr`: Declination in radians
- `dbhr`: Horizontal field component in radians
- `mfig`: Magnetic field intensity
- `mfir`: Magnetic field intensity in radians
- `mdig`: Magnetic declination inclination in degrees
- `mdir`: Magnetic declination inclination in radians

Load your data into a pandas DataFrame:

```python
import pandas as pd

# Load your magnetic field data
data = pd.read_csv('your_emag_data.csv')

# Ensure data has all required features
features = ['decg', 'dbhg', 'decr', 'dbhr', 'mfig', 'mfir', 'mdig', 'mdir']
X = data[features]
```

### 3. Make Predictions
Use the loaded model to make predictions:

```python
# Make predictions
predictions = model.predict(X)

# Add predictions to your DataFrame
data['predicted_earthquake'] = predictions
```

### 4. Set Up Alerts
To set up an alert system, you can use Python to send an email or trigger a notification when an earthquake is predicted.

Example using `smtplib` to send an email:

```python
import smtplib
from email.mime.text import MIMEText

def send_alert(email_subject, email_body, to_email):
    from_email = 'your_email@example.com'
    msg = MIMEText(email_body)
    msg['Subject'] = email_subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'your_password')
        server.sendmail(from_email, to_email, msg.as_string())

# Example usage
if data['predicted_earthquake'].sum() > 0:  # If any earthquakes are predicted
    send_alert('Earthquake Prediction Alert', 'Potential earthquake detected. Please take necessary precautions.', 'recipient_email@example.com')
```

### 5. Continuous Monitoring (Optional)
For continuous monitoring, you can set up a script to fetch new magnetic data periodically and run the prediction model, sending alerts as needed.

### 6. Additional Tips
- Ensure your magnetic data is accurate and up-to-date for best prediction results.
- Customize the alert system according to your needs (e.g., SMS, Slack notifications).

## Conclusion
By following these steps, you can use the trained earthquake prediction model to analyze magnetic data and predict potential seismic activity. Ensure you regularly update your data and monitor model performance for optimal results.

