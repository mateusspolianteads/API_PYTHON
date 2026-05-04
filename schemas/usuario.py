from pydantic import BaseModel
from typing import Optional


class UsuarioCreate(BaseModel):
    nome: str
    email: str
    telefone: str
    senha: str


class LoginRequest(BaseModel):
    email: str
    senha: str


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    senha: Optional[str] = None