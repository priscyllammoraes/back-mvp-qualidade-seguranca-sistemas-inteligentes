import pytest
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import os

# Função auxiliar para carregar e pré-processar o dataset de teste
def carregar_dados():
    caminho_csv = os.path.join(os.path.dirname(__file__), '..', 'ml', 'data', 'ObesityDataSet_raw_and_data_sinthetic.csv')
    df = pd.read_csv(caminho_csv)

    # Remove colunas que não são utilizadas na predição
    df = df.drop(columns=['Height', 'Weight'])

    # Arredonda e transforma colunas numéricas discretas em inteiros
    colunas_float_discretas = ['Age', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']
    df[colunas_float_discretas] = df[colunas_float_discretas].round().astype(int)

    # Aplica one-hot encoding nas colunas binárias
    colunas_binarias = ['Gender', 'FHWO', 'FAVC', 'SMOKE', 'SCC']
    df = pd.get_dummies(df, columns=colunas_binarias, drop_first=True)

    # Aplica one-hot encoding nas colunas categóricas com múltiplos valores
    colunas_multiclasse = ['CAEC', 'CALC', 'MTRANS']
    df = pd.get_dummies(df, columns=colunas_multiclasse, drop_first=False)

    return df

# Testa o desempenho do modelo SVM otimizado usando os dados completos
def test_modelo_otimizado_svm():
    df = carregar_dados()

    # Carrega o modelo treinado a partir do arquivo salvo
    caminho_modelo = os.path.join(os.path.dirname(__file__), '..', 'ml', 'model', 'modelo_otimizado_svm_original.pkl')
    modelo = joblib.load(caminho_modelo)

    # Separa variáveis independentes (X) e variável alvo (y)
    y = df['NObeyesdad']
    X = df.drop(columns=['NObeyesdad'])

    # Ajusta X para ter as mesmas colunas que o modelo espera
    X = X.reindex(columns=modelo.feature_names_in_, fill_value=0)

    # Realiza predições com o modelo carregado
    y_pred = modelo.predict(X)

    # Codifica os rótulos reais para compatibilidade com as predições
    label_encoder = LabelEncoder()
    label_encoder.fit(y)
    y_encoded = label_encoder.transform(y)

    # Calcula a acurácia entre os rótulos previstos e os reais (codificados)
    accuracy = accuracy_score(y_encoded, y_pred)


    # Impressões auxiliares para depuração e verificação de consistência
    print("Distribuição de classes:")
    print(y.value_counts())


    print("\n====== DEBUG TESTE MODELO SVM ======")
    print(f"Número de amostras: {len(X)}")
    print(f"Colunas do X: {list(X.columns)}")
    print(f"Acurácia do modelo SVM: {accuracy:.4f}")
    print("====================================\n")

    print("Distribuição de predições:")
    print(pd.Series(y_pred).value_counts())

    print("Distribuição real:")
    print(y.value_counts())

    print("Primeiras predições vs reais:")
    print(list(zip(y_pred[:10], y[:10])))

    # Verifica se o modelo atende ao desempenho mínimo
    assert accuracy >= 0.78

