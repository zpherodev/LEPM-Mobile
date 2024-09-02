from sklearn.model_selection import train_test_split

# Function to create mock data (repeated for continuity in the corrected code)
def create_mock_data(num_samples, anomaly=True, noise=False):
    np.random.seed(42)  # For reproducibility
    dates = pd.date_range(start="2024-01-01", periods=num_samples, freq='D')
    if anomaly:
        # Generate magnetic anomaly data with clear patterns before earthquakes
        decg = np.sin(np.linspace(0, 20, num_samples)) + np.random.normal(0, 0.1, num_samples)
        dbhg = np.cos(np.linspace(0, 20, num_samples)) + np.random.normal(0, 0.1, num_samples)
    elif noise:
        # Generate random noise data with no clear patterns
        decg = np.random.normal(0, 1, num_samples)
        dbhg = np.random.normal(0, 1, num_samples)
    else:
        # Generate normal data with no anomalies
        decg = np.random.normal(0, 0.1, num_samples)
        dbhg = np.random.normal(0, 0.1, num_samples)
    
    earthquakes = np.zeros(num_samples)
    if anomaly:
        # Simulate earthquakes happening shortly after anomalies
        earthquake_indices = np.where((decg > 0.8) & (dbhg > 0.8))[0]
        earthquakes[earthquake_indices + 1] = 1  # Earthquake occurs the day after anomaly
    
    data = pd.DataFrame({
        'date': dates,
        'decg': decg,
        'dbhg': dbhg,
        'earthquake': earthquakes
    })
    
    return data

# Create mock datasets
data_a = create_mock_data(100, anomaly=True, noise=False)  # Clear anomalies
data_b = create_mock_data(100, anomaly=False, noise=False) # No anomalies
data_c = create_mock_data(100, anomaly=False, noise=True)  # Random noise

# Prepare datasets for model testing
datasets = {'Dataset A': data_a, 'Dataset B': data_b, 'Dataset C': data_c}

# Initialize Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Evaluate model on each dataset
results = {}
for name, data in datasets.items():
    # Prepare features and labels
    X = data[['decg', 'dbhg']]
    y = data['earthquake']
    
    # Train/test split (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    rf_model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = rf_model.predict(X_test)
    
    # Evaluate the model
    report = classification_report(y_test, y_pred, output_dict=True)
    cm = confusion_matrix(y_test, y_pred)
    
    # Store results
    results[name] = {'classification_report': report, 'confusion_matrix': cm}

# Display the results
results