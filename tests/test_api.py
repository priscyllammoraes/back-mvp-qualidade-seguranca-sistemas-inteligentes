import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import json
from app import app
from model import Session, Pessoa

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def exemplo_pessoa():
    return {
        "Age": 28, "FCVC": 3, "NCP": 4, "CH2O": 2, "FAF": 1, "TUE": 2,
        "Gender": "Female", "FHWO": "yes", "FAVC": "yes", "SMOKE": "no",
        "SCC": "no", "CAEC": "Sometimes", "CALC": "Frequently", "MTRANS": "Walking"
    }

def test_home_redirect(client):
    response = client.get("/")
    assert response.status_code == 302
    assert "/openapi" in response.location


def test_predict_route():
    exemplo_predicao = {
        "Age": "30", "FCVC": "3", "NCP": "3", "CH2O": "2", "FAF": "2",
        "TUE": "1", "Gender": "Female", "FHWO": "yes", "FAVC": "yes",
        "SMOKE": "no", "SCC": "no", "CAEC": "Always","CALC": "Frequently","MTRANS": "Walking"
    }

    with app.test_client() as client:
        response = client.post("/predict", data=exemplo_predicao, content_type="multipart/form-data")
        assert response.status_code == 200
        assert "prediction" in response.json


def test_criar_pessoa():
    exemplo_pessoa = {
        "Age": "28",
        "FCVC": "3",
        "NCP": "4",
        "CH2O": "2",
        "FAF": "1",
        "TUE": "2",
        "Gender": "Female",
        "FHWO": "yes",
        "FAVC": "yes",
        "SMOKE": "no",
        "SCC": "no",
        "CAEC": "Sometimes",
        "CALC": "Frequently",
        "MTRANS": "Walking"
    }

    with app.test_client() as client:
        response = client.post("/pessoa", data=exemplo_pessoa, content_type="multipart/form-data")

        # Verificações
        assert response.status_code == 200
        assert "prediction" in response.json

        # Checa se todos os campos obrigatórios estão no retorno
        esperado = [
            "Age", "FCVC", "NCP", "CH2O", "FAF", "TUE", "Gender",
            "FHWO", "FAVC", "SMOKE", "SCC", "CAEC", "CALC", "MTRANS", "prediction"
        ]
        for campo in esperado:
            assert campo in response.json



def test_listar_pessoas(client):
    response = client.get("/pessoas")
    assert response.status_code == 200
    assert "pessoas" in response.json
    assert isinstance(response.json["pessoas"], list)

def test_deletar_pessoa(client, exemplo_pessoa):
    # Cria pessoa
    client.post("/pessoa", data=exemplo_pessoa, content_type="multipart/form-data")

    # Captura ID
    with Session() as session:
        ultima = session.query(Pessoa).order_by(Pessoa.id.desc()).first()
        id_pessoa = ultima.id

    # Remove
    response = client.delete(f"/pessoa?id={id_pessoa}")
    assert response.status_code == 200
    assert "mensagem" in response.json
    assert response.json["mensagem"] == "Pessoa removido"


