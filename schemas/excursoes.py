from pydantic import BaseModel
from typing import Optional


class ExcursaoCreate(BaseModel):
    destino: str
    evento: str
    data: str
    horario: str
    valor: float
    vagas: int

    
class ExcursaoUpdate(BaseModel):
    destino: Optional[str] = None
    evento: Optional[str] = None
    data: Optional[str] = None
    horario: Optional[str] = None
    valor: Optional[float] = None
    vagas: Optional[int] = None