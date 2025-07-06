import pytest

from pydantic import ValidationError

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from schema.obesidade_schema import ObesidadeInputSchema


# Exemplo de payload vindo do frontend
payload_frontend = {
    "Age": 55,
    "FCVC": 1,
    "NCP": 1,
    "CH2O": 1,
    "FAF": 0,
    "TUE": 0,
    "Gender": "Female",
    "FHWO": "yes",
    "FAVC": "yes",
    "CAEC": "no",
    "SMOKE": "yes",
    "SCC": "yes",
    "CALC": "no",
    "MTRANS": "Automobile"
}


def test_payload_valido_pelo_schema():
    try:
        schema = ObesidadeInputSchema(**payload_frontend)
        assert isinstance(schema, ObesidadeInputSchema)
    except ValidationError as e:
        pytest.fail(f"Payload inválido para o schema: {e.json()}")

