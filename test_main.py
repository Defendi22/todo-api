import pytest
from fastapi.testclient import TestClient
from app.main import app

# TestClient simula requisições HTTP sem precisar subir o servidor
client = TestClient(app)


# --- Testes do health check ---

def test_raiz_retorna_ok():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


# --- Testes de criar tarefa ---

def test_criar_tarefa():
    response = client.post("/tarefas", json={
        "titulo": "Comprar pão",
        "descricao": "Padaria da esquina"
    })
    assert response.status_code == 201
    dados = response.json()
    assert dados["titulo"] == "Comprar pão"
    assert dados["concluida"] == False
    assert "id" in dados


def test_criar_tarefa_sem_titulo_retorna_erro():
    response = client.post("/tarefas", json={
        "descricao": "Sem título"
    })
    assert response.status_code == 422  # Unprocessable Entity


# --- Testes de listar tarefas ---

def test_listar_tarefas():
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert "tarefas" in response.json()


# --- Testes de buscar tarefa ---

def test_buscar_tarefa_existente():
    # Primeiro cria
    criar = client.post("/tarefas", json={"titulo": "Tarefa teste"})
    tarefa_id = criar.json()["id"]

    # Depois busca
    response = client.get(f"/tarefas/{tarefa_id}")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarefa teste"


def test_buscar_tarefa_inexistente():
    response = client.get("/tarefas/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada"


# --- Testes de atualizar tarefa ---

def test_atualizar_tarefa():
    criar = client.post("/tarefas", json={"titulo": "Antes"})
    tarefa_id = criar.json()["id"]

    response = client.patch(f"/tarefas/{tarefa_id}", json={
        "titulo": "Depois",
        "concluida": True
    })
    assert response.status_code == 200
    assert response.json()["titulo"] == "Depois"
    assert response.json()["concluida"] == True


def test_atualizar_tarefa_inexistente():
    response = client.patch("/tarefas/99999", json={"titulo": "X"})
    assert response.status_code == 404


# --- Testes de deletar tarefa ---

def test_deletar_tarefa():
    criar = client.post("/tarefas", json={"titulo": "Deletar isso"})
    tarefa_id = criar.json()["id"]

    response = client.delete(f"/tarefas/{tarefa_id}")
    assert response.status_code == 204

    # Confirma que sumiu
    buscar = client.get(f"/tarefas/{tarefa_id}")
    assert buscar.status_code == 404


def test_deletar_tarefa_inexistente():
    response = client.delete("/tarefas/99999")
    assert response.status_code == 404