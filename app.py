from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from datetime import timedelta
from dao.usuario_dao import get_db_connection
from routes.usuarios import usuarios_bp
from routes.artistas import artistas_bp
from routes.empresa import empresas_bp
from routes.vagas import vagas_bp
from routes.auth import auth_bp, blacklist

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'sua-chave-secreta-muito-secreta'  # Altere para uma chave segura em produção
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Token expira em 1 hora

jwt = JWTManager(app)
bcrypt = Bcrypt(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in blacklist

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
app.register_blueprint(artistas_bp, url_prefix="/artistas")
app.register_blueprint(empresas_bp, url_prefix="/empresas")
app.register_blueprint(vagas_bp, url_prefix="/vagas")

def criarTabelas():
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS artistas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            area TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empresas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vagas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            salario FLOAT NOT NULL,
            localizacao TEXT NOT NULL,
            requisito TEXT NOT NULL,
            descricao TEXT NOT NULL,            
            empresa_id INTEGER NOT NULL,
            FOREIGN KEY (empresa_id) REFERENCES empresas(id) ON DELETE CASCADE
        )
    """)

    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criarTabelas()
    app.run(debug=True)