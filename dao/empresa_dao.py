from dao.usuario_dao import get_db_connection

class EmpresaDAO:
    @staticmethod
    def insert_empresa(usuario_id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
            INSERT INTO empresas(usuario_id)
            VALUES (?);
            ''',
            (usuario_id,)
        )
        conexao.commit()
        conexao.close()
    @staticmethod
    def get_all_empresas():
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM usuarios WHERE categoria = "Empresa";
            '''
        )
        empresas = cursor.fetchall()
        empresaDict = [dict(a) for a in empresas]
        conexao.close()
        return empresaDict

    @staticmethod
    def select_empresa_by_id(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM usuarios WHERE id = ? AND categoria = "Empresa";
            '''
            , (id, )
        )
        row = cursor.fetchone()
        conexao.close()
        if row: 
            return dict(row)
        return None

    @staticmethod
    def select_empresa_by_username(username):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM usuarios WHERE username = ? AND categoria = "Empresa";
            '''
            , (username, )
        )
        row = cursor.fetchone()
        conexao.close()
        if row: 
            return dict(row)
        return None

    @staticmethod
    def update_empresa_by_id(username, nome, email, senha, id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                UPDATE usuarios
                SET username = ?, nome = ?, email = ?, senha = ?
                WHERE id = ? AND categoria = "Empresa";
            '''
            , (username, nome, email, senha, id)
        )
        conexao.commit()
        conexao.close()

    @staticmethod
    def delete_empresa_by_id(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                DELETE FROM usuarios
                WHERE id = ? AND categoria = "Empresa";
            '''
            , (id, )
        )
        conexao.commit()
        conexao.close()

