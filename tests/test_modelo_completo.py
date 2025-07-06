import pytest
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
import os


# Parâmetros    
url_dados = "./ml/data/ObesityDataSet_raw_and_data_sinthetic.csv"

# Parâmetros    
url_dados = "./MachineLearning/data/test_dataset_diabetes.csv"
colunas = ['Age', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE',
    'Gender', 'FHWO', 'FAVC', 'SMOKE', 'SCC',
    'CAEC', 'CALC', 'MTRANS']
colunas_finais = ['Age', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE',
    'Gender_Male', 'FHWO_yes', 'FAVC_yes', 'SMOKE_yes', 'SCC_yes',
    'CAEC_Always', 'CAEC_Frequently', 'CAEC_Sometimes', 'CAEC_no',
    'CALC_Always', 'CALC_Frequently', 'CALC_Sometimes', 'CALC_no',
    'MTRANS_Automobile', 'MTRANS_Bike', 'MTRANS_Motorbike',
    'MTRANS_Public_Transportation', 'MTRANS_Walking']


# Carrega o dataset de teste
def carregar_dados():
    caminho_csv = os.path.join(os.path.dirname(__file__), '..', 'ml', 'data', 'ObesityDataSet_raw_and_data_sinthetic.csv')
    df = pd.read_csv(caminho_csv)

    # Pré-processamento conforme notebook do projeto
    df = df.drop(columns=['Height', 'Weight'])

    colunas_float_discretas = ['Age', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']
    df[colunas_float_discretas] = df[colunas_float_discretas].round().astype(int)

    colunas_binarias = ['Gender', 'FHWO', 'FAVC', 'SMOKE', 'SCC']
    df = pd.get_dummies(df, columns=colunas_binarias, drop_first=True)

    colunas_multiclasse = ['CAEC', 'CALC', 'MTRANS']
    df = pd.get_dummies(df, columns=colunas_multiclasse, drop_first=False)

    return df

# Teste do modelo otimizado (SVM)
def test_modelo_otimizado_svm():
    df = carregar_dados()
    # Garante que X tenha as mesmas colunas que o modelo espera
    colunas_esperadas = modelo.feature_names_in_
    X = X.reindex(columns=colunas_esperadas, fill_value=0)
    y = df['NObeyesdad']

    caminho_modelo = os.path.join(os.path.dirname(__file__), '..', 'ml', 'model', 'modelo_otimizado_svm_original.pkl')
    modelo = joblib.load(caminho_modelo)

    y_pred = modelo.predict(X)
    acuracia = accuracy_score(y, y_pred)

    print(f"Acurácia do modelo SVM: {acuracia:.4f}")

    assert acuracia >= 0.78

