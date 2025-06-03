// magnetometer_client.js
// Live client-side magnetometer uploader for Capacitor/React Native using expo-sensors

import { Magnetometer } from 'expo-sensors';
import * as Location from 'expo-location';

const API_URL = './flask/submitMagnetometerData';

// Get current geolocation
async function getLocation() {
  try {
    let { status } = await Location.requestForegroundPermissionsAsync();
    if (status !== 'granted') {
      console.warn('Location permission not granted');
      return { lat: null, lon: null };
    }
    let location = await Location.getCurrentPositionAsync({});
    return {
      lat: location.coords.latitude,
      lon: location.coords.longitude
    };
  } catch (e) {
    console.error('Location error:', e);
    return { lat: null, lon: null };
  }
}

// Initialize magnetometer and send data on interval
let subscription = null;
function startMagnetometerLogging() {
  Magnetometer.setUpdateInterval(10000); // 10 seconds

  subscription = Magnetometer.addListener(async (data) => {
    const { x: bx, y: by, z: bz } = data;
    const { lat, lon } = await getLocation();

    const payload = {
      bx: parseFloat(bx.toFixed(3)),
      by: parseFloat(by.toFixed(3)),
      bz: parseFloat(bz.toFixed(3)),
      lat,
      lon,
      timestamp: new Date().toISOString()
    };

    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      const result = await res.json();
      console.log('[MAGNETIC RESPONSE]', result);

      if (result.prediction === 1) {
        alert(`⚠️ Geomagnetic Event Detected\nConfidence: ${result.confidence * 100}%`);
      }
    } catch (err) {
      console.error('Error sending magnetometer data:', err);
    }
  });
}

// To stop listening:
function stopMagnetometerLogging() {
  if (subscription) {
    subscription.remove();
    subscription = null;
  }
}

// Example usage:
startMagnetometerLogging();
