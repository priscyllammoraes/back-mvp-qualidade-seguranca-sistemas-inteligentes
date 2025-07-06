from sqlalchemy import Column, String, Integer
from model import Base

# Define a tabela "pessoas" com os atributos usados na predição
class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column("Age", Integer)
    fcvc = Column("Fcvc", Integer)
    ncp = Column("Ncp", Integer)
    ch2o = Column("Ch2o", Integer)
    faf = Column("Faf", Integer)
    tue = Column("Tue", Integer)
    gender = Column("Gender", String(50))
    fhwo = Column("Fhwo", String(50))
    favc = Column("Favc", String(50))
    caec = Column("Caec", String(50))
    smoke = Column("Smoke", String(50))
    scc = Column("Scc", String(50))
    calc = Column("Calc", String(50))
    mtrans = Column("Mtrans", String(50))
    prediction = Column("Prediction", String(100)) # Resultado da predição de obesidade

    def __init__(
    self,
    Age: int, FCVC: int, NCP: int, CH2O: int, FAF: int, TUE: int,
    Gender: str, FHWO: str, FAVC: str, CAEC: str,
    SMOKE: str, SCC: str, CALC: str, MTRANS: str,
    prediction: str = None 
    ):
        self.age = Age
        self.fcvc = FCVC
        self.ncp = NCP
        self.ch2o = CH2O
        self.faf = FAF
        self.tue = TUE
        self.gender = Gender
        self.fhwo = FHWO
        self.favc = FAVC
        self.caec = CAEC
        self.smoke = SMOKE
        self.scc = SCC
        self.calc = CALC
        self.mtrans = MTRANS
        self.prediction = prediction


    def to_dict(self):
        """Retorna os dados da pessoa no formato de dicionário."""
        return {
            "Age": self.age,
            "FCVC": self.fcvc,
            "NCP": self.ncp,
            "CH2O": self.ch2o,
            "FAF": self.faf,
            "TUE": self.tue,
            "Gender": self.gender,
            "FHWO": self.fhwo,
            "FAVC": self.favc,
            "CAEC": self.caec,
            "SMOKE": self.smoke,
            "SCC": self.scc,
            "CALC": self.calc,
            "MTRANS": self.mtrans
        }

    def __str__(self):
        return f"Pessoa({self.to_dict()})"
