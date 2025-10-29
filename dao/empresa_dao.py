from dao.usuario_dao import get_db_connection

class EmpresaDAO:
    @staticmethod
    def insert_empresa(usuario_id):
        conexao = get_db_connection()

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE id = ?", 
            (usuario_id,))
        
        if not cursor.fetchone():
            raise ValueError("USUARIO_NAO_ENCONTRADO")
        
        cursor.execute(
            "SELECT * FROM empresas WHERE usuario_id = ?", 
            (usuario_id,)
        )
        if cursor.fetchone():
            raise ValueError("EMPRESA_JA_EXISTE")
        
        cursor.execute(
            '''
            INSERT INTO empresas(usuario_id)
            VALUES (?);
            ''',
            (usuario_id,)
        )

        conexao.commit()

        empresa_id = cursor.lastrowid
        cursor.execute("SELECT * FROM artistas WHERE id = ?;", (empresa_id,))
        empresa = dict(cursor.fetchone())

        cursor.close()
        conexao.close()
        return empresa
        
    @staticmethod
    def get_all_empresas():
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT DISTINCT u.id, u.username, u.nome, u.email, u.senha
                from usuarios u
                INNER JOIN empresas e ON u.id = e.usuario_id;
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
                SELECT DISTINCT u.id, u.username, u.nome, u.email, u.senha
                from usuarios u
                JOIN empresas e ON u.id = e.usuario_id
                WHERE u.id = ? AND u.categoria = "Empresa";
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
                SELECT u.id, u.username, u.nome, u.email, u.senha
                from usuarios u
                JOIN empresas e ON u.id = e.usuario_id
                WHERE u.username = ? AND u.categoria = "Empresa";
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

