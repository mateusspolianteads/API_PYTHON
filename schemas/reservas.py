from pydantic import BaseModel
from typing import Optional


class ReservaCreate(BaseModel):
    cliente_id: int
    excursao_id: int
    quantidade_passagens: int


class ReservaUpdate(BaseModel):
    cliente_id: Optional[int] = None
    excursao_id: Optional[int] = None
    quantidade_passagens: Optional[int] = None