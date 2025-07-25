# -*- coding: utf-8 -*-
"""stress_score_fusion

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XwUeXg0Jszderdq60DrM6zuUq4k7zHjo
"""

"""
Fuse scores from all modality tanh outputs into one overall weighted score
"""
import pandas as pd
import numpy as np

MODALITY_FILES = [
    "exports/behavior_stress_scores.xlsx",
    "exports/ppg_stress_scores.xlsx",
    "exports/spo2_stress_scores.xlsx",
    "exports/face_emotion_scores.xlsx",
    "exports/speech_emotion_scores.xlsx"
]

def fuse_scores():
    all_scores = []
    for file in MODALITY_FILES:
        df = pd.read_excel(file)
        all_scores.append(df["tanh_score"].values[:len(all_scores[0]) if all_scores else None])

    fused = np.mean(np.vstack(all_scores), axis=0)
    result_df = pd.DataFrame({
        "Fused Stress Score": fused,
        "Interpretation": np.where(fused > 0.3, "High Stress",
                          np.where(fused < -0.3, "Non-Stress", "Moderate Stress"))
    })
    result_df.to_excel("exports/fused_stress_scores.xlsx", index=False)
    print("Fused scores saved to exports/fused_stress_scores.xlsx.")

if __name__ == "__main__":
    fuse_scores()