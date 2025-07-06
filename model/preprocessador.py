import pandas as pd
import pandas as pd
from model.constantes import COLUNAS_FINAIS

def preprocessar_entrada(dados_brutos: dict) -> pd.DataFrame:
    """Recebe dados brutos do usuário e retorna DataFrame pré-processado para o modelo."""

    print("📥 Dados brutos recebidos:")
    print(dados_brutos)

    # Conversão de tipos para inteiros nos campos numéricos
    campos_int = ['Age', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']
    for campo in campos_int:
        dados_brutos[campo] = int(dados_brutos[campo])

    print("\n✅ Dados após conversão de tipos:")
    print(dados_brutos)

    # Criar DataFrame a partir do dicionário
    df = pd.DataFrame([dados_brutos])
    print("\n🧾 DataFrame inicial:")
    print(df)

    # Aplicar one-hot encoding (binárias com drop_first, multiclasses completas)
    df_encoded = pd.get_dummies(df, columns=[
        'Gender', 'FHWO', 'FAVC', 'SMOKE', 'SCC'
    ], drop_first=True)

    df_encoded = pd.get_dummies(df_encoded, columns=[
        'CAEC', 'CALC', 'MTRANS'
    ], drop_first=False)

    print("\n🔄 DataFrame após one-hot encoding:")
    print(df_encoded)

    print("\n🧩 Colunas geradas:")
    print(df_encoded.columns.tolist())

    # Preencher colunas ausentes com 0
    for coluna in COLUNAS_FINAIS:
        if coluna not in df_encoded:
            df_encoded[coluna] = 0

    # Garantir a ordem correta das colunas
    df_encoded = df_encoded[COLUNAS_FINAIS]
    print("\n📊 DataFrame final ajustado para o modelo (colunas ordenadas):")
    print(df_encoded)

    return df_encoded


