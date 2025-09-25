from dao.vaga_dao import VagaDAO
from dao.empresa_dao import EmpresaDAO



def criarVaga(dados):
    
    empresa = EmpresaDAO.select_empresa_by_id(dados["empresa_id"])
    if not empresa:
        return None, "EMPRESA_NAO_ENCONTRADA"

    
    VagaDAO.insert_vaga(
        dados["titulo"],
        dados["salario"],
        dados["localizacao"],
        dados["requisito"],
        dados["descricao"],
        dados["empresa_id"]
    )
   
    todas = VagaDAO.get_all_vagas()
    return todas[-1], None

def listarVagas():
    return VagaDAO.get_all_vagas()

def buscarVagaPorId(id):
    vaga = VagaDAO.select_vaga_by_id(id)

    if not vaga:
        return None, "VAGA_NAO_ENCONTRADO"
    
    return vaga, None

def buscarVagaPorTitulo(titulo):
    vaga = VagaDAO.select_vaga_by_titulo(titulo)

    if not vaga:
        return None, "VAGA_NAO_ENCONTRADA"
    
    return vaga, None

def buscarVagaPorEmpresa(empresa_id):
    empresa = EmpresaDAO.select_empresa_by_id(empresa_id)

    if not empresa:
        return None, "EMPRESA_NAO_ENCONTRADA"
    return VagaDAO.select_vaga_by_empresa(empresa_id), None

def editarVaga(id, novosDados):
    vagaEncontrada, erro = buscarVagaPorId(id)
    if erro:
        return None, "VAGA_NAO_ENCONTRADA"
    
        
    vagaAtual = vagaEncontrada
    titulo = novosDados.get("titulo", vagaAtual["titulo"])
    salario = novosDados.get("salario", vagaAtual["salario"])
    localizacao = novosDados.get("localizacao", vagaAtual["localizacao"])
    requisito = novosDados.get("requisito", vagaAtual["requisito"])
    descricao = novosDados.get("descricao", vagaAtual["descricao"])

    VagaDAO.update_vaga_by_id(id, titulo, salario, localizacao, requisito, descricao)
    vagaAtualizada = VagaDAO.select_vaga_by_id(id)
    return vagaAtualizada, None

    
def deletarVaga(id):
    vaga, erro = buscarVagaPorId(id)
    if erro:
        return False, "VAGA_NAO_ENCONTRADA"
    
    VagaDAO.delete_vaga_by_id(id)
    return True, None