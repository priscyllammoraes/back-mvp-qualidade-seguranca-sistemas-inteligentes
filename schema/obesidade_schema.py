from pydantic import BaseModel
from typing import List
from typing import Literal
from model.constantes import LABELS


# Schema para entrada de dados de predição direta (sem salvar no banco)
class ObesidadeInputSchema(BaseModel):
    Age: int
    FCVC: int
    NCP: int
    CH2O: int
    FAF: int
    TUE: int
    Gender: Literal["Female", "Male"]
    FHWO: Literal["yes", "no"]
    FAVC: Literal["yes", "no"]
    SMOKE: Literal["yes", "no"]
    SCC: Literal["yes", "no"]
    CAEC: Literal["no", "Sometimes", "Frequently", "Always"]
    CALC: Literal["no", "Sometimes", "Frequently", "Always"]
    MTRANS: Literal[
        "Automobile", "Motorbike", "Bike",
        "Public_Transportation", "Walking"
    ]

    class Config:
        schema_extra = {
            "example": {
                "Age": 21,
                "FCVC": 3,
                "NCP": 4,
                "CH2O": 2,
                "FAF": 1,
                "TUE": 2,
                "Gender": "Female",
                "FHWO": "yes",
                "FAVC": "yes",
                "SMOKE": "no",
                "SCC": "no",
                "CAEC": "Sometimes",
                "CALC": "Frequently",
                "MTRANS": "Walking"
            }
        }


# Schema para resposta da predição
class ObesidadeResultSchema(BaseModel):
    prediction: str


# Função que converte o código da predição em rótulo textual
def apresenta_predicao(pred) -> dict:
    try:
        classe = int(pred)
        return {"prediction": LABELS.get(classe, f"Classe {classe}")}
    except:
        return {"prediction": str(pred)}



