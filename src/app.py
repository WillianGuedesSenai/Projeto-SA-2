from flask import Flask, g
import sqlite3

from utils import Logger

log = Logger("App", enabled=True)

app = Flask(__name__, template_folder="pages", static_folder="static")

DATABASE = 'automax.db'

def get_db():
    db = getattr(g, '_database', None)
    
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  
    
    return db
    
    
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Importa as rotas DEPOIS de criar o app
from routes import home 
from routes import produto  # ← SINGULAR!


# Este bloco só executa se rodar com "python app.py"
if __name__ == "__main__":
    log.info("Iniciando servidor Flask...")
    app.run(debug=True, host='0.0.0.0', port=5000)