from fastapi import APIRouter, HTTPException
from database import clientes

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.get("/")
def listar():
    return clientes


@router.post("/")
def criar(cliente: dict):
    cliente["id"] = len(clientes) + 1
    clientes.append(cliente)
    return cliente


@router.delete("/{id}")
def deletar(id: int):
    for cliente in clientes:
        if cliente["id"] == id:
            clientes.remove(cliente)
            return {"mensagem": "Removido"}
    raise HTTPException(status_code=404, detail="Não encontrado")