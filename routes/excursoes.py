from datetime import date

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

    if excursao.data < date.today():
        raise HTTPException(
            status_code=400, detail="A data da excursão deve ser hoje ou futura"
        )

    nova_excursao = excursao.model_dump()
    nova_excursao["id"] = len(excursoes) + 1
    excursoes.append(nova_excursao)

    return {"mensagem": "Excursão cadastrada com sucesso", "excursao": nova_excursao}


@router.patch("/{id}")
def atualizar(id: int, dados: ExcursaoUpdate):
    for excursao in excursoes:
        if excursao["id"] == id:
            dados_atualizados = dados.model_dump(exclude_unset=True, exclude_none=True)

            excursao.update(dados_atualizados)

            return {"mensagem": "Excursão atualizada com sucesso", "excursao": excursao}

    raise HTTPException(status_code=404, detail="Excursão não encontrada")


@router.delete("/{id}")
def deletar(id: int):
    for excursao in excursoes:
        if excursao["id"] == id:
            excursoes.remove(excursao)
            return {"mensagem": "Excursão removida com sucesso"}

    raise HTTPException(status_code=404, detail="Excursão não encontrada")
