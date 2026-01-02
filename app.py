import streamlit as st
import xgboost as xgb
from xgboost import DMatrix
import numpy as np
import librosa
import os

# Model path
model_path = 'models/diabetes_voice_female.json'
if not os.path.exists(model_path):
    st.error(f"Model file not found at {model_path}. Run the notebook to train and save it first!")
    st.stop()

# Load as Booster
model = xgb.Booster()
model.load_model(model_path)

st.title("Diabetes Risk Screening from Voice")

st.write("Upload a 6-10 second WAV file saying: 'Hello, how are you today?'")

audio_file = st.file_uploader("Upload WAV file", type=["wav"])

if audio_file is not None:
    # Load audio
    y, sr = librosa.load(audio_file, sr=None)
    
    # Placeholder features (replace with real extraction later)
    features = np.random.rand(1, 1026)
    
    # Predict
    dmatrix = DMatrix(features)
    probabilities = model.predict(dmatrix)[0]
    predicted_class = np.argmax(probabilities)
    
    risk_levels = {0: "Low", 1: "Moderate", 2: "High", 3: "Very High"}
    
    st.write("Probability for each risk level:")
    for i, prob in enumerate(probabilities):
        level = risk_levels.get(i, f"Class {i}")
        st.progress(float(prob))
        st.write(f"{level}: {prob:.1%}")