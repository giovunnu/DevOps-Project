import random
from fastapi import FastAPI
from pydantic import BaseModel
import secrets

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

@app.get("/helloworld")
async def root():
    return {"Hello": "World"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": secrets.randbelow(1004)}


@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante


@app.put("/estudante/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0


@app.delete("/estudante/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0

#Criação de Personagem em Jogo

def criar_personagem(nome, idade, tipo, forca, habilidade):
    if not nome:
        raise ValueError("O nome não pode estar vazio")

    if not tipo:
        raise ValueError("O tipo não pode estar vazio")

    while idade <= 10:
        raise ValueError("A idade deve ser maior que 10")

    if not (1 <= forca <= 100):
        raise ValueError("Força deve estar entre 1 e 100")

    return {
        "Nome": nome,
        "Idade": idade,
        "Tipo": tipo,
        "Força": forca,
        "Habilidade Especial": habilidade
    }



