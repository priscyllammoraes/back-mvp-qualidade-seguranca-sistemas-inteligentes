from model.model_loader import load_model

# Carrega o modelo uma vez, ao iniciar o módulo
model = load_model()

def predict(df_input):
    """Recebe um DataFrame de entrada e retorna a predição (classe) como inteiro."""
    pred = model.predict(df_input)
    return int(pred[0])


