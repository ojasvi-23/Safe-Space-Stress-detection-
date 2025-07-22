# Safe-Space-Stress-detection-
# 🧠 Per-Feature Explainable Multimodal Stress Detection and Feedback System

This project is a **real-time stress detection system** that leverages physiological, behavioral, and emotional modalities to classify stress and generate personalized natural language feedback using a locally-hosted LLM (e.g., Mistral-7B-Instruct).

---

## 📦 Features

- Real-time fusion of:
  - **Heart Rate Variability (PPG from WESAD)**
  - **SpO₂ (from BIDMC dataset)**
  - **Behavioral inputs** (Keystroke + Mouse activity)
  - **Facial Emotion Recognition** (FER-2013)
  - **Speech Emotion Recognition** (RAVDESS / TESS)
- **Tanh-normalized stress score** output in range `[-1, +1]`
- Final fused score mapped to:
  - High Stress
  - Moderate Stress
  - Non-Stress
- Natural Language **narrative feedback** generation using rules or LLM


---

## 🛠 Installation

```bash
pip install numpy pandas matplotlib scikit-learn joblib librosa openpyxl


| Modality        | Dataset        | Model               | Accuracy |
| --------------- | -------------- | ------------------- | -------- |
| Keystroke/Mouse | Custom         | XGBoost             | \~81%    |
| HRV (PPG)       | WESAD          | Logistic Regression | \~87%    |
| SpO₂            | BIDMC          | Logistic Regression | \~89%    |
| Face Emotion    | FER-2013       | Logistic Regression | \~77%    |
| Speech Emotion  | RAVDESS / TESS | Logistic Regression | \~83%    |

# Train individual models
python models/train_keystroke_mouse.py
python models/train_ppg_pulse.py
python models/train_spo2_model.py
python models/train_face_emotion.py
python models/train_speech_emotion.py

# Fuse the stress scores
python models/stress_score_fusion.py

# Generate feedback using LLM or template rules
python models/generate_feedback.py
📘 Citation
“Per-Feature Explainable Multimodal Stress Detection and Narrative Feedback System” — 2025 (under submission)


🌟 Acknowledgements
WESAD (Wearable Stress and Affect Detection)

BIDMC SpO₂ dataset

FER-2013, RAVDESS, and TESS datasets

LangChain, HuggingFace, Mistral
