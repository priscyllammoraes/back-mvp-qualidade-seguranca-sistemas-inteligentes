
# Predição de Obesidade - API

Este projeto foi desenvolvido como parte do MVP da disciplina **Qualidade, Segurança e Sistemas Inteligentes**, com o objetivo de prever o grau de obesidade de um indivíduo com base em seus hábitos e informações pessoais.

A API recebe os dados do usuário, realiza o pré-processamento, faz a predição com base em um modelo treinado e opcionalmente armazena os dados no banco. Todas as interações seguem o padrão REST e contam com validação usando Pydantic.

---

## Tecnologias Utilizadas

- **Python 3.11**
- **Flask**
- **Flask-CORS**
- **Flask-OpenAPI3**
- **SQLAlchemy**
- **SQLite**
- **Pydantic**
- **Scikit-learn**
- **Docker (opcional)**

---

## Funcionalidades da API

### Predição (sem salvar)
- **POST** `/predict`  
  Realiza a predição do grau de obesidade com base nos dados informados (formulário).

### Cadastro de Pessoa (com predição e salvamento)
- **POST** `/pessoa`  
  Realiza a predição e salva a pessoa no banco de dados.

### Listar Pessoas
- **GET** `/pessoas`  
  Retorna todas as pessoas cadastradas com suas respectivas predições.

### Remover Pessoa
- **DELETE** `/pessoa?id=<id>`  
  Remove a pessoa do banco de dados.

### Verificação da API
- **GET** `/health`  
  Verifica se a aplicação está rodando corretamente.

---

## Estrutura do Projeto

```
mvp-backend/
├── ml/
│   └── data/
│   │   └── ObesityDataSet_raw_and_data_sinthetic.csv
│   └── model/
│   │   └── modelo_otimizado_svm_original.pkl
│   └── notebook/
│   │   └── MVP_Modelo_Obesidade.ipynb
├── model/
│   └── base.py
│   └── constantes.py
│   └── model_loader.py
│   └── pessoa.py
│   └── predictor.py
│   └── preprocessador.py
├── schema/
│   ├── pessoa_schema.py
│   ├── obesidade_schema.py
│   └── error_schema.py
├── tests/
│   └── test_api.py
│   └── test_modelo.py
│   └── test_validacao_payload.py
├── requirements.txt
└── README.md
```

---

## Executando Localmente

### 1. Clonar o Repositório

```bash
git clone https://github.com/priscyllammoraes/back-mvp-qualidade-seguranca-sistemas-inteligentes
cd back-mvp-qualidade-seguranca-sistemas-inteligentes
```

### 2. Instalar dependências

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. Executar a aplicação

```bash
flask run --host 0.0.0.0 --port 5000
```

A API estará disponível em: [http://localhost:5000](http://localhost:5000)

---

## Testes Automatizados

Os testes foram escritos com **pytest** e cobrem as principais rotas da API, além do desempenho do modelo de machine learning.

⚠️ Importante: Para que os imports funcionem corretamente, os testes devem ser executados a partir da pasta tests.
Use o comando abaixo para entrar na pasta e rodar os testes:

### Rodar os testes:

```bash
cd tests
pytest -s test_api.py
pytest -s test_modelo.py
```

---

## Exemplo de Payload

```json
{
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
```

---

## Autora

- **Priscylla Moraes**  
  GitHub: [@priscyllammoraes](https://github.com/priscyllammoraes)
