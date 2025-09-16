from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# importa a conexão com o banco
from app.core import database
from app.api.v1.endpoints import transactions, categories, reports

# cria a aplicação FastAPI
app = FastAPI(
    title="Finance Control API",
    description="API para controle de finanças pessoais (entradas, saídas, relatórios e saldo por categoria).",
    version="1.0.0",
)

# Middleware de CORS (caso vá consumir com frontend ou mobile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois restringe p/ domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# inclui as rotas
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["Transactions"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["Categories"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])

# evento de inicialização (ex: criar tabelas se não tiver migrations ainda)
@app.on_event("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)

# rota simples para testar se está no ar
@app.get("/")
def root():
    return {"message": "🚀 Finance Control API is running!"}
