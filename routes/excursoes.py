from fastapi import APIRouter, HTTPException
from database import excursoes
from schemas.excursoes import ExcursaoCreate, ExcursaoUpdate

router = APIRouter(prefix="/excursoes", tags=["Excursões"])


@router.get("/")
def listar():
    return excursoes


@router.get("/{id}")
def listar_por_id(id: int):
    for excursao in excursoes:
        if excursao["id"] == id:
            return excursao
    raise HTTPException(status_code=404, detail="Excursão não encontrada")


@router.post("/cadastrar")
def cadastrar(excursao: ExcursaoCreate):
    nova_excursao = excursao.dict()
    nova_excursao["id"] = len(excursoes) + 1
    excursoes.append(nova_excursao)

    return {
        "mensagem": "Excursão cadastrada com sucesso",
        "excursao": nova_excursao
    }


@router.patch("/{id}")
def atualizar(id: int, dados: ExcursaoUpdate):
    for excursao in excursoes:
        if excursao["id"] == id:
            excursao.update(dados.dict(exclude_unset=True))
            return excursao

    raise HTTPException(status_code=404, detail="Excursão não encontrada")


@router.delete("/{id}")
def deletar(id: int):
    for excursao in excursoes:
        if excursao["id"] == id:
            excursoes.remove(excursao)
            return {"mensagem": "Excursão removida"}

    raise HTTPException(status_code=404, detail="Excursão não encontrada")