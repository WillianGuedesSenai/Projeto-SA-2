from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def home_alt():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Importa as rotas de produtos
import routes.produto