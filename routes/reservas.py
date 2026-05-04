from fastapi import APIRouter, HTTPException
from database import reservas
from schemas.reservas import ReservaCreate, ReservaUpdate

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.get("/")
def listar():
    return reservas


@router.get("/{id}")
def listar_por_id(id: int):
    for reserva in reservas:
        if reserva["id"] == id:
            return reserva
    raise HTTPException(status_code=404, detail="Reserva não encontrada")


@router.post("/cadastrar")
def cadastrar(reserva: ReservaCreate):
    nova_reserva = reserva.dict()
    nova_reserva["id"] = len(reservas) + 1
    reservas.append(nova_reserva)

    return {
        "mensagem": "Reserva cadastrada com sucesso",
        "reserva": nova_reserva
    }


@router.patch("/{id}")
def atualizar(id: int, dados: ReservaUpdate):
    for reserva in reservas:
        if reserva["id"] == id:
            reserva.update(dados.dict(exclude_unset=True))
            return reserva

    raise HTTPException(status_code=404, detail="Reserva não encontrada")


@router.delete("/{id}")
def deletar(id: int):
    for reserva in reservas:
        if reserva["id"] == id:
            reservas.remove(reserva)
            return {"mensagem": "Reserva removida"}

    raise HTTPException(status_code=404, detail="Reserva não encontrada")