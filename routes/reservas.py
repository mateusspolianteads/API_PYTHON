from fastapi import APIRouter, HTTPException
from database import usuarios

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.get("/")
def listar():
    return usuarios


@router.get("/{id}")
def listar_por_id(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@router.post("/cadastrar")
def cadastrar(usuario: dict):
    for u in usuarios:
        if usuario["email"] == u["email"]:
            raise HTTPException(status_code=400, detail="Já existe um usuário com esse email")

    usuario["id"] = len(usuarios) + 1
    usuarios.append(usuario)
    return {"mensagem": "Usuário cadastrado com sucesso", "usuario": usuario}


@router.post("/login")
def login(dados: dict):
    for usuario in usuarios:
        if usuario["email"] == dados["email"] and usuario["senha"] == dados["senha"]:
            return {"mensagem": "Login realizado com sucesso"}
    raise HTTPException(status_code=401, detail="Email ou senha inválidos")


@router.patch("/{id}")
def atualizar(id: int, dados: dict):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario.update(dados)
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@router.delete("/{id}")
def deletar(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
