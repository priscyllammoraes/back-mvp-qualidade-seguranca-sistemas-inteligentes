from pathlib import Path
import joblib
import pandas as pd
from model.constantes import COLUNAS_FINAIS

def test_modelo_carrega_e_prediz():
    modelo_path = Path("ml/model/modelo_otimizado_svm_original.pkl")
    assert modelo_path.exists(), "Modelo .pkl não encontrado"

    modelo = joblib.load(modelo_path)

    # Cria dict com todas as colunas do modelo com valor 0
    exemplo_dict = {col: 0 for col in COLUNAS_FINAIS}
    # Preenche manualmente alguns campos
    exemplo_dict.update({
        "Age": 34,
        "FCVC": 2,
        "NCP": 3,
        "CH2O": 2,
        "FAF": 1,
        "TUE": 1,
        "Gender_Male": 1,
        "FHWO_yes": 1,
        "FAVC_yes": 1,
        "SMOKE_yes": 0,
        "SCC_yes": 0,
        "CAEC_Sometimes": 1,
        "CALC_Sometimes": 1,
        "MTRANS_Public_Transportation": 1
    })

    exemplo = pd.DataFrame([exemplo_dict])[COLUNAS_FINAIS]  # Garante ordem

    resultado = modelo.predict(exemplo)
    assert resultado is not None
    assert len(resultado) == 1
