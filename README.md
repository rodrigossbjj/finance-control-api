# Finance Control API

API RESTful para controle de finanças pessoais, desenvolvida com **FastAPI**, **PostgreSQL** e **SQLAlchemy**.  
Oferece autenticação com JWT, cadastro de usuários, categorias e transações financeiras.

---

## 🚀 Tecnologias
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Pydantic](https://docs.pydantic.dev/)

---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/finance-control-api.git
   cd finance-control-api
   ```

2. Crie um arquivo `.env` na raiz do projeto:
   ```env
   DATABASE_URL=postgresql://usuario:senha@db:5432/finance_db
   SECRET_JWT=sua_chave_secreta
   ```

3. Suba os containers com Docker:
   ```bash
   docker-compose up --build
   ```

---

## 📌 Endpoints

### 🔑 Usuários (`/users`)
- `POST /users/register` → Cria um novo usuário (e-mail + senha).  
- `POST /users/login` → Faz login e retorna o **JWT** para autenticação.

### 🏷️ Categorias (`/categories`)
- `GET /categories/` → Lista todas as categorias do usuário logado.  
- `GET /categories/{category_id}` → Retorna os detalhes de uma categoria específica.  
- `POST /categories/` → Cria uma nova categoria.  
- `PUT /categories/{category_id}` → Atualiza uma categoria existente.  
- `DELETE /categories/{category_id}` → Remove uma categoria.

### 💰 Transações (`/transactions`)
- `GET /transactions/` → Lista todas as transações do usuário logado.  
- `GET /transactions/{transaction_id}` → Retorna os detalhes de uma transação.  
- `POST /transactions/` → Cria uma nova transação.  
- `PUT /transactions/{transaction_id}` → Atualiza uma transação existente.  
- `DELETE /transactions/{transaction_id}` → Remove uma transação.

---

## 🔒 Autenticação
- Todas as rotas (exceto **/users/register** e **/users/login**) exigem um **JWT válido**.  
- Enviar no header:
  ```http
  Authorization: Bearer <token>
  ```

---

## 🛠️ Estrutura do Projeto
```
finance-control-api/
│── app/
│   ├── api/           # Rotas da API
│   ├── core/          # Configurações principais (DB, segurança, auth)
│   ├── models/        # Modelos do banco de dados
│   ├── schemas/       # Schemas Pydantic
│   └── repositories/  # Repositórios de acesso ao banco
│── .env.example       # Exemplo de variáveis de ambiente
│── docker-compose.yml # Configuração Docker
│── requirements.txt   # Dependências
│── README.md          # Documentação
```

---

## 📄 Licença
Este projeto está sob a licença MIT.  
Sinta-se livre para usá-lo e contribuir! 🚀
