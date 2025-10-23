import sqlite3

DATABASE = "usuario.db"

def get_db_connection():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao

class UsuarioDAO:
    @staticmethod
    def insert_user(username, nome, email, senha, categoria):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                INSERT INTO usuarios(username, nome, email, senha, categoria) VALUES (?, ?, ?, ?, ?);
            '''
            , (username, nome, email, senha, categoria)
        )
        conexao.commit()
        conexao.close()

    @staticmethod
    def get_all_users():
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM usuarios;
            '''
        )
        usuarios = cursor.fetchall()
        usuarioDict = [dict(u) for u in usuarios]
        conexao.close()
        return usuarioDict

    @staticmethod
    def select_user_by_id(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM usuarios WHERE id = ?;
            '''
            , (id, )
        )
        row = cursor.fetchone()
        conexao.close()
        if row: 
            return dict(row)
        return None

    @staticmethod
    def select_user_by_username(username):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM usuarios WHERE username = ?;
            '''
            , (username, )
        )
        row = cursor.fetchone()
        conexao.close()
        if row: 
            return dict(row)
        return None
    
    @staticmethod
    def update_user_by_id(username, nome, email, senha, categoria, id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                UPDATE usuarios
                SET username = ?, nome = ?, email = ?, senha = ?, categoria = ?
                WHERE id = ?;
            '''
            , (username, nome, email, senha, categoria, id)
        )
        conexao.commit()
        conexao.close()

    @staticmethod
    def delete_user_by_id(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                DELETE FROM usuarios
                WHERE id = ?;
            '''
            , (id, )
        )
        conexao.commit()
        conexao.close()

