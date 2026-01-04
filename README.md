# AI Voice Detection for Diabetes Risk Screening

An AI tool that screens for type 2 diabetes risk using voice analysis.  
Built with deep voice embeddings from the **VOCADIAB** dataset, age, BMI, and an XGBoost classifier.

**Demo**: Upload a short WAV file to get an instant risk prediction.

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/ai-voice-diabetes-detection.git
cd ai-voice-diabetes-detection

python -m venv .venv
source .venv/bin/activate    # macOS/Linux
# .venv\Scripts\activate     # Windows

pip install -r requirements.txt

streamlit run app.py


📊 Key Features

Predicts diabetes risk level (Low / Moderate / High / Very High)
Uses pre-trained Byol-S voice embeddings + age & BMI
Streamlit web interface for easy testing
Trained on real clinical voice data (VOCADIAB)


🗂️ Project Structure
textAI_VOICE_DETECTION_FOR_DIABETES/
├── data/vocadiab/          # Dataset
├── models/                 # Saved model
├── notebooks/exploration.ipynb  # Training notebook
├── src/app.py              # Streamlit app
├── requirements.txt
└── README.md

🔬 Research Basis
Based on VOCADIAB (Colive Voice study)
Voice changes linked to diabetes (e.g., neuropathy, dehydration)
Note: Research prototype for screening only — not a medical diagnosis.

📈 Future Ideas
Real-time audio feature extraction (pitch, jitter, shimmer)
Male model + gender selection
Browser voice recording
Public online deployment

🤝 Contributing
Pull requests welcome! Open issues for bugs or suggestions.

📄 License
MIT License
Built with Python, XGBoost, Streamlit, and VOCADIAB 🚀
textJust replace `yourusername/ai-voice-diabetes-detection` with your actual GitHub repo URL.