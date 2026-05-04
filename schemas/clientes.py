from pydantic import BaseModel
from typing import Optional


class ClienteCreate(BaseModel):
    nome: str
    email: str
    telefone: str
    cpf: str


class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    cpf: Optional[str] = None