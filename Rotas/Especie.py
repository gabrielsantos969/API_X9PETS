from FuncoesDeAPI import TimeExecute
from flask import jsonify
from flask import request, Response
from BancoDeDados.store import bancoSupabase
from BancoDeDados.store import add_especie, update_especie

""" ============================= BUSCA DE DADOS NO BANCO ================================================== """
""" Pega todas as especies que tem no banco de dados """
def TodasEspecies():
    try:
        start = TimeExecute.StartTime()
        allEspecies = bancoSupabase.table("TP_ESPECIE").select("*").execute()
        end = TimeExecute.EndTime()
        count = len(allEspecies.data)

        if count != 0:
            return jsonify({
                "especies": allEspecies.data,
                "message": f'Foram encontradas {count} especies.',
                "time_execute": f'{TimeExecute.MsgResultTime(end, start)}'
            }), 200
        else:
            return Response('''{"message": "Não foi encontrado nenhuma especie!"}''', status=400, mimetype='application/json')

    except:
        return Response('''{"message": "Ainda não há especies cadastrados no sistema"}''', status=400, mimetype='application/json')

""" ============================================== FUNCOES DE METODO POST ===================================================== """
""" Faz o cadastro de uma especie no banco de dados """
def CadastrarEspecie():
    data = request.get_json()

    try:
        nmEspecie = data['nm_especie']
        cdEspecie = data['cd_especie']
 

        if isinstance(nmEspecie, str) and isinstance(cdEspecie, int):

            dataCadastro = add_especie(nmEspecie, cdEspecie)

            return dataCadastro, 201
        else: 
            return jsonify({
                "message": "Erro no envio dos dados passados!"
            }), 400
    except:
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')

""" Atualiza uma especie conforme o ID da especie """
def AtualizarDadosEspecie(id_especie):

    dados = request.get_json()

    try:
        nameEspecie = dados['nm_especie']
        
       
        id = int(id_especie)
        if isinstance(id, int):
            updateData = update_especie(id, nameEspecie)
            return updateData
        else:
            return jsonify({
                "message": "O parâmetro passado não é permitido!"
            }), 400

    except:
        return Response('''{"message": "Algo deu errado na atualização!"}''', status=400, mimetype='application/json')