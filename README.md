
# Predição de Obesidade - API

Este projeto foi desenvolvido como parte do MVP da disciplina **Qualidade e Segurança de Sistemas Inteligentes**, com o objetivo de prever o grau de obesidade de um indivíduo com base em seus hábitos e informações pessoais.

A API recebe os dados do usuário, realiza o pré-processamento, faz a predição com base em um modelo treinado e opcionalmente armazena os dados no banco. Todas as interações seguem o padrão REST e contam com validação robusta usando Pydantic.

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

### 🔍 Predição (sem salvar)
- **POST** `/predict`  
  Realiza a predição do grau de obesidade com base nos dados informados (formulário).

### 🧍 Cadastro de Pessoa (com predição e salvamento)
- **POST** `/pessoa`  
  Realiza a predição e salva a pessoa no banco de dados.

### 📋 Listar Pessoas
- **GET** `/pessoas`  
  Retorna todas as pessoas cadastradas com suas respectivas predições.

### 🔎 Buscar Pessoa por ID
- **GET** `/pessoa?id=<id>`  
  Retorna os dados e predição de uma pessoa específica com base no ID.

### ❌ Remover Pessoa
- **DELETE** `/pessoa?id=<id>`  
  Remove a pessoa do banco de dados.

### ✅ Verificação da API
- **GET** `/health-check`  
  Verifica se a aplicação está rodando corretamente.

---

## Estrutura do Projeto

```
mvp-backend/
├── app.py
├── model/
│   └── pessoa.py
├── schema/
│   ├── pessoa_schema.py
│   ├── obesidade_schema.py
│   └── error_schema.py
├── model/
│   └── modelo.pkl
├── requirements.txt
├── tests/
│   └── test_api.py
└── README.md
```

---

## Executando Localmente

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd mvp-backend
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

Os testes foram escritos com **pytest** e cobrem todas as rotas principais da API.

### Rodar os testes:

```bash
pytest tests/test_api.py
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

## Autor

- **Priscylla Moraes**  
  GitHub: [@priscyllammoraes](https://github.com/priscyllammoraes)
