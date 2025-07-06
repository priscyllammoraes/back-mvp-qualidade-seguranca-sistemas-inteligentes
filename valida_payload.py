from schema.obesidade_schema import ObesidadeInputSchema
from pydantic import ValidationError

payload = {
    "Age": 34,
    "FCVC": 2,
    "NCP": 3,
    "CH2O": 2,
    "FAF": 1,
    "TUE": 1,
    "Gender": "Male",
    "FHWO": "yes",
    "FAVC": "yes",
    "SMOKE": "no",
    "SCC": "no",
    "CAEC": "Sometimes",
    "CALC": "Sometimes",
    "MTRANS": "Walking"
}

try:
    obj = ObesidadeInputSchema(**payload)
    print("✅ Payload válido!")
except ValidationError as e:
    print("❌ Payload inválido:")
    print(e.json(indent=2))
