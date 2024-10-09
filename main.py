from re import template
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from repositories.produto_repo import inserir, criar_tabela
from models.produto_model import Produto 
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def startup():
    criar_tabela()
    
@app.get("/") 
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

# @app.post("/post_cadastro")
# def post_cadastro(
#     request: Request,
#     nome: str = Form(...),
#     estoque: str = Form(...), 
#     preco: str = Form(...),
#     descricao: str = Form(...),
#     categoria: str = Form(...)):
#     return RedirectResponse("/", 303)
@app.post("/post_cadastro")
def post_cadastro(
    request: Request,
    nome: str = Form(...),
    estoque: str = Form(...), 
    preco: str = Form(...),
    descricao: str = Form(...),
    categoria: str = Form(...)):
    
    # Cria o objeto Produto com os dados do formulário
    produto = Produto(
        nome=nome,
        estoque=estoque,
        preco=preco,
        descricao=descricao,
        categoria=categoria
    )
    
    # Tenta inserir o produto no banco de dados
    produto_inserido = inserir(produto)
    
    # Verifica se a inserção foi bem-sucedida
    if produto_inserido:
        return RedirectResponse("/cadastro_recebido", 303)  # Redireciona em caso de sucesso
    else:
        return RedirectResponse("/cadastro", 303)  # Redireciona em caso de falha
 

@app.get("/cadastro_recebido")
def get_contato_recebido(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})
   
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)