from fastapi import APIRouter, HTTPException
from database import excursoes

router = APIRouter(prefix="/excursoes", tags=["Excursões"])


@router.get("/")
def listar():
    return excursoes


@router.post("/")
def criar(excursao: dict):
    excursao["id"] = len(excursoes) + 1
    excursoes.append(excursao)
    return excursao


@router.delete("/{id}")
def deletar(id: int):
    for excursao in excursoes:
        if excursao["id"] == id:
            excursoes.remove(excursao)
            return {"mensagem": "Removida"}
    raise HTTPException(status_code=404, detail="Não encontrada")