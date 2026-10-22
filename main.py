from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"mensagem": "API ativa"}


@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    # Regra corrigida na Parte 3
    return {"resultado": a + b}


@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    # Rota adicionada na Parte 3
    return {"resultado": a * b}