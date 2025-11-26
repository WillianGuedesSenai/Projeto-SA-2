import sqlite3
from flask import render_template
from app import app
from app import get_db

DATABASE = 'automax.db'

@app.route('/produtos/<int:id>')
def get_product(id):
    db = get_db()
    cursor = db.cursor()
    
    
    return "Não encontramos o produto!"
    
    
    
    #produto_dict = {
     #   "id": produto['id_peca'],
      #  "nome": produto['nome_peca'],
       ##"tipo": produto['tipo']
   # } 