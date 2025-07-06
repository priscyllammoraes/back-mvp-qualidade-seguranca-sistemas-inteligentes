from pydantic import BaseModel
from typing import List, Literal
from model.pessoa import Pessoa

# Schema de entrada para adicionar e prever uma nova pessoa (com salvamento no banco)
class PessoaSchema(BaseModel):
    """Define como uma nova pessoa deve ser representada para predição"""
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
    MTRANS: Literal["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"] 

    class Config:
        schema_extra = {
            "example": {
                "Age": 28,
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


# Schema de visualização com predição
class PessoaViewSchema(BaseModel):
    """Define como uma predição de pessoa será retornada"""
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
    MTRANS: Literal["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"]
    prediction: str

    class Config:
        schema_extra = {
            "example": {
                "Age": 28,
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
                "MTRANS": "Walking",
                "prediction": "Sobrepeso Nível I (IMC 25,0 – 27,4)"
            }
        }

class PessoaIdSchema(BaseModel):
    """
    Schema para representar a busca de pessoa com base no ID.
    """
    id: int  # ID da pessoa

# Lista de pessoas com predição
class ListaPessoasSchema(BaseModel):
    """Define como uma lista de predições será representada"""
    pessoas: List[PessoaViewSchema]

# Schema para buscar uma pessoa (por id)
class PessoaBuscaSchema(BaseModel):
    """Define como buscar uma pessoa pelo ID (Futuramente)"""
    id: int

# Função auxiliar para serializar uma pessoa com predição
def apresenta_pessoa(pessoa: Pessoa, prediction: str):
    return {
        "id": pessoa.id,
        "Age": pessoa.age,
        "FCVC": pessoa.fcvc,
        "NCP": pessoa.ncp,
        "CH2O": pessoa.ch2o,
        "FAF": pessoa.faf,
        "TUE": pessoa.tue,
        "Gender": pessoa.gender,
        "FHWO": pessoa.fhwo,
        "FAVC": pessoa.favc,
        "CAEC": pessoa.caec,
        "SMOKE": pessoa.smoke,
        "SCC": pessoa.scc,
        "CALC": pessoa.calc,
        "MTRANS": pessoa.mtrans,
        "prediction": prediction
    }


# Função auxiliar para serializar lista de pessoas
def apresenta_pessoas(pessoas: List[Pessoa]):
    result = []
    for p in pessoas:
        result.append({
            "id": p.id,
            "Age": p.age,
            "Gender": p.gender,
            "FHWO": p.fhwo,
            "FAVC": p.favc,            
            "FCVC": p.fcvc,
            "NCP": p.ncp,
            "CAEC": p.caec,
            "SMOKE": p.smoke,
            "CH2O": p.ch2o,
            "SCC": p.scc,
            "FAF": p.faf,
            "TUE": p.tue,  
            "CALC": p.calc,
            "MTRANS": p.mtrans,
            "prediction": p.prediction            
        })
    return {"pessoas": result}

