import joblib
from pathlib import Path

# Caminho do modelo treinado e salvo (formato .pkl)
MODEL_PATH = Path(__file__).resolve().parents[1] / "ml" / "model" / "modelo_otimizado_svm_original.pkl"

def load_model():
    """Carrega e retorna o modelo treinado a partir do arquivo .pkl"""
    return joblib.load(MODEL_PATH)