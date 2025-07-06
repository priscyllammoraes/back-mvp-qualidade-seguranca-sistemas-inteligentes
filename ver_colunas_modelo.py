# ver_colunas_modelo.py
import joblib
from pathlib import Path

modelo_path = Path("ml/model/modelo_obesidade_svm_padronizado.pkl")
model = joblib.load(modelo_path)

colunas = []

# Tenta extrair as colunas diretamente
if hasattr(model, "feature_names_in_"):
    colunas = list(model.feature_names_in_)
else:
    try:
        preproc = model.named_steps.get("preprocessor")
        if preproc and hasattr(preproc, "transformers"):
            for nome, transformer, cols in preproc.transformers:
                colunas.extend(cols)
    except Exception as e:
        print("Erro ao tentar extrair colunas do pré-processador:", e)

print("Colunas usadas no modelo:")
print(colunas)
