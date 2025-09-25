from dao.usuario_dao import get_db_connection
from models.artista import Artista


class ArtistaDAO:
    @staticmethod
    def insert_artista(username, nome, email, senha, area):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                INSERT INTO usuarios(username, nome, email, senha, categoria, area) VALUES (?, ?, ?, ?, "Artista", ?);
            '''
            , (username, nome, email, senha, area)
        )
        conexao.commit()
        conexao.close()

    @staticmethod
    def get_all_artistas():
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM usuarios WHERE categoria = "Artista";
            '''
        )
        artistas = cursor.fetchall()
        artistaDict = [dict(a) for a in artistas]
        conexao.close()
        return artistaDict

    @staticmethod
    def select_artista_by_id(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM usuarios WHERE id = ? AND categoria = "Artista";
            '''
            , (id, )
        )
        artista = dict(cursor.fetchone())
        conexao.close()
        return artista

    @staticmethod
    def select_artista_by_username(username):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM usuarios WHERE username = ? AND categoria = "Artista";
            '''
            , (username, )
        )
        artista = dict(cursor.fetchone())
        conexao.close()
        return artista

    @staticmethod
    def update_artista_by_id(username, nome, email, senha, area, id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                UPDATE usuarios
                SET username = ?, nome = ?, email = ?, senha = ?, area = ?
                WHERE id = ? AND categoria = "Artista";
            '''
            , (username, nome, email, senha, area, id)
        )
        conexao.commit()
        conexao.close()

    @staticmethod
    def delete_artista_by_id(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                DELETE FROM usuarios
                WHERE id = ? AND categoria = "Artista";
            '''
            , (id, )
        )
        conexao.commit()
        conexao.close()

