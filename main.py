from re import template
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/") 
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
def get_contato(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro")
def post_contato(
    request: Request, 
    nome: str = Form(...), 
    estoque: str = Form(...), 
    preco: str = Form(...),
    descricao: str = Form(...)):
    return RedirectResponse("/cadastro_recebido", 303)
@app.get("/cadastro_recebido")
def cadastro_recebido(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})
   

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)