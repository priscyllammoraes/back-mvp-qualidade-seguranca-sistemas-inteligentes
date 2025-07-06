# Lista das colunas finais que o modelo espera após o pré-processamento (com one-hot encoding)
COLUNAS_FINAIS = [
    'Age', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE',
    'Gender_Male', 'FHWO_yes', 'FAVC_yes', 'SMOKE_yes', 'SCC_yes',
    'CAEC_Always', 'CAEC_Frequently', 'CAEC_Sometimes', 'CAEC_no',
    'CALC_Always', 'CALC_Frequently', 'CALC_Sometimes', 'CALC_no',
    'MTRANS_Automobile', 'MTRANS_Bike', 'MTRANS_Motorbike',
    'MTRANS_Public_Transportation', 'MTRANS_Walking'
]


# Mapeamento de rótulos para classes preditas
LABELS = {
    0: "Peso Insuficiente (IMC < 18,5)",
    1: "Peso Normal (IMC 18,5 – 24,9)",
    2: "Obesidade Grau I (IMC 30,0 – 34,9)",
    3: "Obesidade Grau II (IMC 35,0 – 39,9)",
    4: "Obesidade Grau III (IMC ≥ 40)",
    5: "Sobrepeso Nível I (IMC 25,0 – 27,4)",
    6: "Sobrepeso Nível II (IMC 27,5 – 29,9)"
}