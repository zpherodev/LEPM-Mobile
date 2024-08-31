
# Earthquake Prediction Model Files

This repository contains the data and trained model files for predicting earthquakes with magnitudes of 6.0 to 9.0 and above using geomagnetic field parameters.

## Files

1. **merged_earthquake_m9_data.csv**: The merged dataset containing earthquake data for magnitudes 9.0 and above from 1924 to 2024, as well as other data for 6 and above, and 7 and above, all combined with corresponding magnetic field parameters.
   - **Columns**: `earthquake_date`, `latitude`, `longitude`, `decg`, `dbhg`, `decr`, `dbhr`, `mfig`, `mfir`, `mdig`, `mdir`, `magnitude`, `decr_above_new`, `mdig_above_new`

2. **random_forest_model_m9.pkl**: The trained Random Forest model for predicting earthquakes of magnitude 6.0 and above.
   - This model was trained using a Random Forest classifier with 100 trees and a random state of 42 for reproducibility.

3. **scaler_m9.pkl**: The scaler used for feature standardization.
   - The features were standardized using a StandardScaler to ensure that they have a mean of 0 and a standard deviation of 1.

## Usage

- **Load the Data**: Use the `merged_earthquake_m9_data.csv` to load the data for analysis or further model training.
- **Load the Model**: Use `joblib` to load the `random_forest_model_m9.pkl` for making predictions.
  ```python
  import joblib
  model = joblib.load('random_forest_model_m9.pkl')
  ```
- **Standardize Features**: Use the `scaler_m9.pkl` to standardize new data before making predictions with the model.
  ```python
  scaler = joblib.load('scaler_m9.pkl')
  X_scaled = scaler.transform(new_data)
  ```

## Future Steps

1. **Expand Data**: Continue collecting more data across different regions and magnitudes to improve model generalization.
2. **Model Refinement**: Experiment with different models or additional features to enhance prediction accuracy.
3. **Deployment**: Consider deploying the model in a cloud environment or as part of an early warning system.

## Contact

For further information or collaboration, please reach out to crk.nft.art@gmail.com

## Acknowledgements

Developed utilizing the amazing skills of ChatGPT 4o made by OpenAI, a thrilling process that deserves much praise to the advancements of the AI model, and a tip of the hat to OpenAI developers and co.

Special Thanks to NOAA, the USGS, the BGS for the use and availability of important data.

