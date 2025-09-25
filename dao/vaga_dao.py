from dao.usuario_dao import get_db_connection

class VagaDAO:
    @staticmethod
    def insert_vaga(titulo, salario, localizacao, requisito, descricao, empresa_id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                INSERT INTO vagas(titulo, salario, localizacao, requisito, descricao, empresa_id) VALUES (?, ?, ?, ?, ?, ?);
            '''
            , (titulo, salario, localizacao, requisito, descricao, empresa_id)
        )
        conexao.commit()
        conexao.close()

    @staticmethod
    def get_all_vagas():
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM vagas;
            '''
        )
        vagas = cursor.fetchall()
        vagaDict = [dict(a) for a in vagas]
        conexao.close()
        return vagaDict

    @staticmethod
    def select_vaga_by_id(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM vagas WHERE id = ?;
            '''
            , (id, )
        )
        vaga = dict(cursor.fetchone())
        conexao.close()
        return vaga

    @staticmethod
    def select_vaga_by_titulo(titulo):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM vagas WHERE titulo = ?;
            '''
            , (titulo, )
        )
        vaga = dict(cursor.fetchone())
        conexao.close()
        return vaga
    
    @staticmethod
    def select_vaga_by_empresa(empresa_id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                SELECT * FROM vagas WHERE empresa_id = ?;
            '''
            , (empresa_id, )
        )
        vaga = dict(cursor.fetchone())
        conexao.close()
        return vaga

    @staticmethod
    def update_vaga_by_id(id, titulo, salario, localizacao, requisito, descricao):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                UPDATE vagas
                SET titulo = ?, salario = ?, localizacao = ?, requisito = ?, descricao = ?
                WHERE id = ?;
            '''
            , (titulo, salario, localizacao, requisito, descricao, id)
        )
        conexao.commit()
        conexao.close()

    @staticmethod
    def delete_vaga_by_id(id):
        conexao = get_db_connection()
        cursor = conexao.cursor()
        cursor.execute(
            '''
                DELETE FROM vagas
                WHERE id = ?;
            '''
            , (id, )
        )
        conexao.commit()
        conexao.close()

