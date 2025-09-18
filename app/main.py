from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importa o router do endpoint de usuários
from app.api.v1.endpoints import users

# Cria a aplicação FastAPI
app = FastAPI(
    title="Finance Control API",
    description="API para controle de finanças pessoais (entradas, saídas e usuários).",
    version="1.0.0",
)

# Middleware de CORS: permite que frontends acessem a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "🚀 Finance Control API is running!"}

@app.on_event("startup")
def startup_event():
    print("API está iniciando...")
