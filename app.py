# Framework e bibliotecas Flask
from sqlite3 import IntegrityError
from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag

# Validação com Pydantic
from pydantic import ValidationError

# Schemas de entrada, saída e formatação
from schema import (ObesidadeInputSchema, ObesidadeResultSchema, PessoaSchema, PessoaViewSchema, PessoaIdSchema, apresenta_pessoa, apresenta_pessoas, apresenta_predicao, ErrorSchema)

# Predição e pré-processamento
from model.predictor import predict
from model.preprocessador import preprocessar_entrada

# Banco de dados e modelo ORM
from model import Session, Pessoa
from logger import logger


# Instanciando o objeto OpenAPI
info = Info(title="API de Predição de Obesidade", version="1.0.0")
app = OpenAPI(
    __name__, info=info, static_folder="../mvp-frontend", static_url_path="/mvp-frontend"
)
CORS(app)


# Definindo tags para agrupamento das rotas
home_tag = Tag(name="documentacao", description="Redireciona para documentação.")
pessoa_tag = Tag(name="pessoa", description="Adição, visualização, remoção e predição de pessoas com obesidade.")
pred_tag = Tag(name="predicao", description="Predição do risco de obesidade sem uso do Banco de Dados.")



# Rota home - redireciona para a documentação Swagger/OpenAPI
@app.get("/", tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect("/openapi")


# Rota de verificação de status da API
@app.get("/health", tags=[home_tag])
def health_check():
    """Verifica o status da API."""
    return {"status": "ok"}


# Rota GET - lista todas as pessoas cadastradas com suas predições
@app.get("/pessoas", tags=[pessoa_tag], responses={"200": PessoaViewSchema, "404": ErrorSchema},)
def get_pessoas():
    """
    Retorna todas as pessoas cadastradas com suas respectivas predições.

    Esta rota consulta o banco de dados e retorna uma lista formatada de registros.
    """
   
    # Criando conexão com a base
    session = Session()
    # Buscando todos os pacientes
    pessoas = session.query(Pessoa).all()

    if not pessoas:
        # Se não houver pacientes
        return {"pacientes": []}, 200
    else:
        
        print(pessoas)
        return apresenta_pessoas(pessoas), 200
    

from fastapi import Body

# Rota POST - adiciona nova pessoa, realiza predição e salva no banco
@app.post("/pessoa",tags=[pessoa_tag], responses={"200": PessoaViewSchema, "400": ErrorSchema, "409": ErrorSchema},)
def adiciona_pessoa(form: PessoaSchema):
    """
    Adiciona uma nova pessoa com os dados fornecidos e retorna a predição do grau de obesidade.

    O registro será salvo no banco de dados. Use esta rota para testes reais com persistência.
    """
    try:
        print(form)
        # Validar dados e preparar para o modelo
        print("------------------gggggggggggggggggggggg-------------------------------")
        dados_dict = form.dict()
        print("------------------gggggggggggggggggggguuuuuuuuuuuuuuuugg-------------------------------")
        dados_processados = preprocessar_entrada(dados_dict)
        resultado = predict(dados_processados)

        # Convertendo a predição em texto para salvar no banco
        classe = apresenta_predicao(resultado)['prediction']

        # Instancia Pessoa com predição
        pessoa = Pessoa(**dados_dict, prediction=classe)

        # Conexão com a base
        session = Session()
        session.add(pessoa)
        session.commit()

        return apresenta_pessoa(pessoa, classe), 200

    except IntegrityError:
        session.rollback()
        logger.warning(f"Erro de integridade ao criar pessoa com idade: '{form.Age}'")
        return {"mensagem": "Erro de integridade ao criar pessoa."}, 409

    except Exception as e:
        session.rollback()
        logger.error(f"Erro inesperado ao criar pessoa: {e}")
        return {"mensagem": f"Erro ao criar pessoa: {str(e)}"}, 400


# Rota DELETE - remove uma pessoa do banco pelo ID
@app.delete("/pessoa", tags=[pessoa_tag], responses={"200": ErrorSchema, "404": ErrorSchema, "500": ErrorSchema})
def deletar_pessoa(query: PessoaIdSchema):
    """
    Remove uma pessoa da base de dados pelo ID.

    Query Parameters:
    - id: inteiro — ID da pessoa a ser excluída
    """
    session = Session()
    try:
        pessoa = session.query(Pessoa).filter(Pessoa.id == query.id).first()
        if not pessoa:
            return {"mensagem": f"Pessoa com ID {query.id} não encontrado."}, 404

        session.delete(pessoa)
        session.commit()
        return {"mensagem": "Pessoa removido", "id": query.id}, 200

    except Exception as e:
        session.rollback()
        return {"mensagem": f"Erro ao deletar pessoa: {str(e)}"}, 500



# Rota POST - realiza predição sem salvar no banco (validação Pydantic ativa)
@app.post("/predict", tags=[pred_tag], responses={"200": ObesidadeResultSchema, "400": ErrorSchema})
def predict_obesidade(form: ObesidadeInputSchema):
    """
    Realiza uma predição de obesidade sem salvar no banco.

    Use esta rota para testar o modelo diretamente, com os dados completos do formulário.
    """

    try:
        print("📩 Dados recebidos no backend (validação Pydantic passou):")
        print(form.dict())
        dados_processados = preprocessar_entrada(form.dict())
        resultado = predict(dados_processados)  # agora passamos o DataFrame direto
        return apresenta_predicao(resultado), 200
    except ValidationError as e:
        ##print("❌ Erro de validação Pydantic:", e.json())
        print("❌ Erro de validação Pydantic:", e.json(indent=2))
        return jsonify({"erro": e.errors()}), 400
    except Exception as ex:
        return jsonify({"erro": f"Erro interno: {str(ex)}"}), 500
    


# # Rota GET - busca uma pessoa pelo ID e retorna seus dados com predição (Futuro)
# @app.get("/pessoa", tags=[pessoa_tag], responses={"200": PessoaViewSchema, "500": ErrorSchema})
# def buscar_pessoa(query: PessoaIdSchema):
#     """
#     Busca uma pessoa cadastrada pelo ID.

#     Parameters:
#     - id: inteiro — ID da pessoa a ser consultada
#     """
#     session = Session()
#     try:
#         pessoa = session.query(Pessoa).filter(Pessoa.id == query.id).first()
#         if not pessoa:
#             return jsonify({"mensagem": "Pessoa não encontrada"}), 404
#         pessoa_dict = PessoaIdSchema.from_orm(pessoa).dict()
#         return jsonify(pessoa_dict), 200

#     except Exception as e:
#         return {"mensagem": f"Erro ao buscar projeto: {str(e)}"}, 500


if __name__ == "__main__":
    app.run(debug=True)
