from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API do Fernando Defendi", version="1.0.20")

# Banco de dados em memória (por enquanto)
tarefas = {}
contador = 1


# Modelo de dados — Pydantic valida automaticamente o que chega
class Tarefa(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False


class TarefaAtualizar(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    concluida: Optional[bool] = None


# GET /         — health check (saber se a API está viva)
@app.get("/")
def raiz():
    return {"status": "ok", "mensagem": "To-Do API funcionando!"}


# GET /tarefas  — lista todas as tarefas
@app.get("/tarefas")
def listar_tarefas():
    return {"tarefas": list(tarefas.values())}


# POST /tarefas — cria uma nova tarefa
@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa):
    global contador
    nova = {"id": contador, **tarefa.model_dump()}
    tarefas[contador] = nova
    contador += 1
    return nova


# GET /tarefas/{id} — busca uma tarefa específica
@app.get("/tarefas/{tarefa_id}")
def buscar_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefas[tarefa_id]


# PATCH /tarefas/{id} — atualiza uma tarefa
@app.patch("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, dados: TarefaAtualizar):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa = tarefas[tarefa_id]
    atualizados = dados.model_dump(exclude_unset=True)
    tarefa.update(atualizados)
    return tarefa


# DELETE /tarefas/{id} — deleta uma tarefa
@app.delete("/tarefas/{tarefa_id}", status_code=204)
def deletar_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    del tarefas[tarefa_id]