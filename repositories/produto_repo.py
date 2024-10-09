from sql.produto_sql import *
from models.produto_model import Produto
from util import obter_conexao
from typing import Optional
from typing import List
from sqlite3 import Connection


def criar_tabela():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA)
        
def inserir(produto: Produto) -> Optional[Produto] :
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_INSERIR, (
            produto.nome,
            produto.descricao,
            produto.estoque,
            produto.preco,
            produto.categoria
        ))
        if db.rowcount > 0:
            produto.id = db.lastrowid
            return produto
        else:
            return None
        
           
def obter_todos(conn: Connection) -> List[Produto]:
    cursor = conn.execute(SQL_OBTER_TODOS)
    produtos = [
        Produto(id=row[0], nome=row[1], descricao=row[2], estoque=row[3], preco=row[4], categoria=row[5])
        for row in cursor.fetchall()
    ]
    return produtos