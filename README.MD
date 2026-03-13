# 📝 To-Do API

API REST completa para gerenciamento de tarefas, construída com FastAPI e Python.

![CI](https://github.com/Defendi22/todo-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 🚀 Demo

API disponível em produção:

```
https://todo-api-xxxx.onrender.com/docs
```

---

## 📋 Funcionalidades

- ✅ Criar tarefas
- ✅ Listar todas as tarefas
- ✅ Buscar tarefa por ID
- ✅ Atualizar tarefa (título, descrição, status)
- ✅ Deletar tarefa
- ✅ Documentação automática (Swagger UI)

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Framework da API |
| [Pydantic](https://docs.pydantic.dev/) | Validação de dados |
| [Uvicorn](https://www.uvicorn.org/) | Servidor ASGI |
| [pytest](https://pytest.org/) | Testes automatizados |
| [Docker](https://www.docker.com/) | Containerização |
| [GitHub Actions](https://github.com/features/actions) | CI/CD |
| [Render](https://render.com/) | Deploy gratuito |

---

## 📁 Estrutura do projeto

```
todo-api/
├── .github/
│   └── workflows/
│       └── ci.yml        # Pipeline CI/CD
├── app/
│   ├── __init__.py
│   └── main.py           # Rotas e lógica da API
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── test_main.py          # Testes automatizados
```

---

## ⚙️ Rodando localmente

### Pré-requisitos

- Python 3.11+
- Docker (opcional)

### Com Python

```bash
# Clone o repositório
git clone https://github.com/Defendi22/todo-api.git
cd todo-api

# Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Rode a API
uvicorn app.main:app --reload
```

Acesse **http://localhost:8000/docs**

### Com Docker

```bash
# Build da imagem
docker build -t todo-api .

# Rode o contêiner
docker run -p 8000:8000 todo-api
```

Acesse **http://localhost:8000/docs**

---

## 🧪 Testes

```bash
pytest -v
```

Resultado esperado:

```
PASSED test_main.py::test_raiz_retorna_ok
PASSED test_main.py::test_criar_tarefa
PASSED test_main.py::test_criar_tarefa_sem_titulo_retorna_erro
PASSED test_main.py::test_listar_tarefas
PASSED test_main.py::test_buscar_tarefa_existente
PASSED test_main.py::test_buscar_tarefa_inexistente
PASSED test_main.py::test_atualizar_tarefa
PASSED test_main.py::test_atualizar_tarefa_inexistente
PASSED test_main.py::test_deletar_tarefa
PASSED test_main.py::test_deletar_tarefa_inexistente

10 passed in 0.45s
```

---

## 📡 Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Health check |
| `GET` | `/tarefas` | Lista todas as tarefas |
| `POST` | `/tarefas` | Cria uma nova tarefa |
| `GET` | `/tarefas/{id}` | Busca uma tarefa pelo ID |
| `PATCH` | `/tarefas/{id}` | Atualiza uma tarefa |
| `DELETE` | `/tarefas/{id}` | Deleta uma tarefa |

### Exemplo de requisição

**POST /tarefas**

```json
{
  "titulo": "Comprar pão",
  "descricao": "Padaria da esquina",
  "concluida": false
}
```

**Resposta 201:**

```json
{
  "id": 1,
  "titulo": "Comprar pão",
  "descricao": "Padaria da esquina",
  "concluida": false
}
```

---

## 🔄 CI/CD

A cada `push` na branch `main`:

1. GitHub Actions roda os testes automaticamente
2. Se os testes passarem, faz o build da imagem Docker
3. Render detecta o push e faz o deploy automático

---

## 📄 Licença

MIT © [Defendi22](https://github.com/Defendi22)