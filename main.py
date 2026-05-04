from fastapi import FastAPI
from routes import usuarios, excursoes, clientes, reservas

app = FastAPI(title="Busão do Rolê API")

app.include_router(usuarios.router)
app.include_router(excursoes.router)
app.include_router(clientes.router)
app.include_router(reservas.router)