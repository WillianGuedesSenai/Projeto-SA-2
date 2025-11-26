# src/routes/produto.py
from flask import render_template
from app import app
import sqlite3

def get_db():
    conn = sqlite3.connect('automax.db')
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

@app.route('/produtos')
def lista_produtos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id_produto, nome, preco, stock FROM produtos ORDER BY nome")
    produtos = cursor.fetchall()
    conn.close()
    return render_template('produtos.html', produtos=produtos)

@app.route('/produto/<int:id>')
def detalhe_produto(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id_produto = ?", (id,))
    produto = cursor.fetchone()
    conn.close()

    if produto is None:
        return "Produto não encontrado!", 404

    return render_template('produto_detalhe.html', produto=produto)