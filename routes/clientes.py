from fastapi import APIRouter, HTTPException
from database import clientes
from schemas.clientes import ClienteCreate, ClienteUpdate

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.get("/")
def listar():
    return clientes


@router.get("/{id}")
def listar_por_id(id: int):
    for cliente in clientes:
        if cliente["id"] == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")


@router.post("/cadastrar")
def cadastrar(cliente: ClienteCreate):
    novo_cliente = cliente.dict()
    novo_cliente["id"] = len(clientes) + 1
    clientes.append(novo_cliente)

    return {
        "mensagem": "Cliente cadastrado com sucesso",
        "cliente": novo_cliente
    }


@router.patch("/{id}")
def atualizar(id: int, dados: ClienteUpdate):
    for cliente in clientes:
        if cliente["id"] == id:
            cliente.update(dados.dict(exclude_unset=True))
            return cliente

    raise HTTPException(status_code=404, detail="Cliente não encontrado")


@router.delete("/{id}")
def deletar(id: int):
    for cliente in clientes:
        if cliente["id"] == id:
            clientes.remove(cliente)
            return {"mensagem": "Cliente removido"}

    raise HTTPException(status_code=404, detail="Cliente não encontrado")