import sqlite3

def popular_produtos():
    conn = sqlite3.connect('automax.db')
    cursor = conn.cursor()
    
    # Limpa a tabela de produtos (opcional - remova se já tiver dados)
    cursor.execute("DELETE FROM produtos")
    
    # Insere produtos de exemplo
    produtos = [
        ("Pastilha de Freio Dianteira Cerâmica", 189.90, 148),
        ("Filtro de Óleo Premium", 45.90, 320),
        ("Kit Amortecedor Completo", 1299.90, 45),
        ("Bateria 60Ah Selada", 389.90, 87),
        ("Disco de Freio Ventilado", 279.90, 92),
        ("Velas de Ignição (Jogo)", 89.90, 215),
        ("Correia Dentada + Kit", 235.90, 68),
        ("Filtro de Ar Esportivo", 125.90, 134),
    ]
    
    cursor.executemany(
        "INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)",
        produtos
    )
    
    conn.commit()
    conn.close()
    print("✅ Produtos inseridos com sucesso!")

if __name__ == '__main__':
    popular_produtos()