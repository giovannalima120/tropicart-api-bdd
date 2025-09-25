from flask import Flask
from dao.usuario_dao import get_db_connection
from routes.usuarios import usuarios_bp

app = Flask(__name__)

def criarTabelaUsuarios():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                categoria TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criarTabelaUsuarios()
    app.run(debug=True)