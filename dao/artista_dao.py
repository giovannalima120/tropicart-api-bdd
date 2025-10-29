from dao.usuario_dao import get_db_connection

class ArtistaDAO:
    @staticmethod
    def insert_artista(usuario_id, area):
        conexao = get_db_connection()

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE id = ?", 
            (usuario_id,))
        
        if not cursor.fetchone():
            raise ValueError("USUARIO_NAO_ENCONTRADO")
        
        cursor.execute(
            "SELECT * FROM artistas WHERE usuario_id = ?", 
            (usuario_id,)
        )
        if cursor.fetchone():
            raise ValueError("ARTISTA_JA_EXISTE")
        
        cursor.execute(
        '''
            INSERT INTO artistas(usuario_id, area)
            VALUES (?, ?);
        ''',
        (usuario_id, area)
        )
        
        conexao.commit()

        artista_id = cursor.lastrowid
        cursor.execute("SELECT * FROM artistas WHERE id = ?;", (artista_id,))
        artista = dict(cursor.fetchone())

        cursor.close()
        conexao.close()

        return artista

    @staticmethod
    def get_all_artistas():
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT DISTINCT u.id, u.username, u.nome, u.email, u.senha, a.area
                from usuarios u
                INNER JOIN artistas a ON u.id = a.usuario_id;
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
                SELECT DISTINCT u.id, u.username, u.nome, u.email, u.senha, a.area
                from usuarios u
                JOIN artistas a ON u.id = a.usuario_id
                WHERE u.id = ? AND u.categoria = "Artista";
            '''
            , (id, )
        )
        row = cursor.fetchone()
        conexao.close()
        if row: 
            return dict(row)
        return None

    @staticmethod
    def select_artista_by_username(username):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT u.id, u.username, u.nome, u.email, u.senha, a.area
                from usuarios u
                JOIN artistas a ON u.id = a.usuario_id
                WHERE u.username = ? AND u.categoria = "Artista";
            '''
            , (username, )
        )
        row = cursor.fetchone()
        conexao.close()
        if row: 
            return dict(row)
        return None

    @staticmethod
    def update_artista_by_id(username, nome, email, senha, area, id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                UPDATE usuarios
                SET username = ?, nome = ?, email = ?, senha = ?
                WHERE id = ? AND categoria = "Artista";
            '''
            , (username, nome, email, senha, id)
        )
        cursor.execute(
            '''
                UPDATE artistas
                SET area = ?
                where usuario_id = ?;
            ''',
            (area, id)
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

