from fastapi import APIRouter, HTTPException
from database import usuarios

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


# Listar todos
@router.get("/")
def listar():
    return usuarios


# Buscar por ID
@router.get("/{id}")
def listar_por_id(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


# Cadastro
@router.post("/cadastro")
def cadastrar(usuario: dict):
    usuario["id"] = len(usuarios) + 1
    usuarios.append(usuario)
    return {
        "mensagem": "Usuário cadastrado com sucesso",
        "usuario": usuario
    }


# Login
@router.post("/login")
def login(dados: dict):
    for usuario in usuarios:
        if usuario["email"] == dados["email"] and usuario["senha"] == dados["senha"]:
            return {"mensagem": "Login realizado com sucesso"}
    raise HTTPException(status_code=401, detail="Email ou senha inválidos")


# Atualizar
@router.patch("/{id}")
def atualizar(id: int, dados: dict):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario.update(dados)
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


# Deletar
@router.delete("/{id}")
def deletar(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")