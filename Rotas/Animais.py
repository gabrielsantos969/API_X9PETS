
from FuncoesDeAPI import TimeExecute
from flask import jsonify
from flask import request, Response
from BancoDeDados.store import bancoSupabase
from BancoDeDados.store import add_pets, update_pets

""" Busca de dados do pet no banco de dados """
def PegarTodosPets():
    try:
        start = TimeExecute.StartTime()
        allPets = bancoSupabase.table("PETS").select("id_pets, pet_name, idade_pet, sn_vacinado, sn_consulta, id_dono_pet(nm_cliente, celular_cliente, email_cliente, cpf_cliente), tp_animal(raca), especie_pet(ds_tp_especie)").execute()
        end = TimeExecute.EndTime()
        count = len(allPets.data)
        if count != 0:
            return jsonify({
                'pets': allPets.data,
                'message': f'Foi encontrado {count} pets no banco de dados',
                'time_execute': f'{TimeExecute.MsgResultTime(end, start)}'
            })
        else:
            return Response('''{"message": "Não foi encontrado nenhum pet"}''', status=400, mimetype='application/json')

    except:
        return Response('''{"message": "Ainda não há animais cadastrados no sistema"}''', status=400, mimetype='application/json')


""" Busca de pet por ID no banco de dados """
def BuscarPetPorId(pet_id):

    try:
        start = TimeExecute.StartTime()
        findPetId = bancoSupabase.table("PETS").select("pet_name, idade_pet, sn_vacinado, sn_consulta, id_dono_pet(nm_cliente, celular_cliente, email_cliente, cpf_cliente), tp_animal(raca), especie_pet(ds_tp_especie)").eq("id_pets", pet_id).execute()
        end = TimeExecute.EndTime()
        count = len(findPetId.data)
        if count != 0:
            return jsonify({
                "filtro_id_pet": findPetId.data,
                'message': f'Foi encontrado {count} pet no banco de dados',
                'time_execute': f'{TimeExecute.MsgResultTime(end, start)}'
            }), 201
        else:
            return Response('''{"message": "Este pet não está cadastrado em nosso sistema."}''', status=400, mimetype='application/json')
    except:
        return Response('''{"message": "Falha ao procurar rota"}''', status=400, mimetype='application/json')

""" Busca de pets por nome no banco de dados """
def BuscarPetPorNome(name_pet):

    try:
        start = TimeExecute.StartTime()
        findPetName = bancoSupabase.table("PETS").select("pet_name, idade_pet, sn_vacinado, sn_consulta, id_dono_pet(nm_cliente, celular_cliente, email_cliente, cpf_cliente), tp_animal(raca), especie_pet(ds_tp_especie)").ilike("pet_name", str(f'%{name_pet}%')).execute()
        end = TimeExecute.EndTime()
        count = len(findPetName.data)

        if count != 0:
            return jsonify({
                "filtro_name_pet": findPetName.data,
                'message': f'Foi encontrado {count} pet(s) no banco de dados.',
                'time_execute': f'{TimeExecute.MsgResultTime(end, start)}'
            }), 201
        else:
            return Response('''{"message": "Nenhum pet com este nome encontrado"}''', status=400, mimetype='application/json')
    except:
        return Response('''{"message": "Algo deu errado"}''', status=400, mimetype='application/json')

""" Deleta o pet por id no banco de dados """
def DeletarPet(id_pet):

    try:
        start = TimeExecute.StartTime()
        deletePet = bancoSupabase.table("PETS").delete().eq("id_pets", id_pet).execute()
        end = TimeExecute.EndTime()
        count = len(deletePet.data)


        if count != 0:
            return jsonify(
                {
                    "Dados apagados": deletePet.data,
                    "message": "Pet exluido do banco de dados!",
                    "time_execute": f'{TimeExecute.MsgResultTime(end, start)}'
                }), 201
        else:
            return Response('''{"message": "O pet que deseja excluir não existe!"}''', status=400, mimetype='application/json')
    
    except:
        return Response('''{"message": "Algo deu errado em sua exclusão, verifique os dados!"}''', status=400, mimetype='application/json')

""" Cadastro um novo pet no banco de dados """
def CadastrarPet():
    data = request.get_json()

    try:
        petName = data['pet_name']
        tpAnimal = data['tp_animal']
        idDono = data['id_dono']
        cdPet = data['cd_pet']
        tpEspecie = data['tp_especie']

        if isinstance(petName, str) and isinstance(tpAnimal, int) and isinstance(idDono, int) and isinstance(cdPet, int) and isinstance(tpEspecie, int):

            dataCadastro = add_pets(petName, tpAnimal, idDono, cdPet, tpEspecie)

            return dataCadastro, 201
        else: 
            return jsonify({
                "message": "Erro no envio dos dados passados!"
            }), 400
    except:
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')

""" Atualiza um pet atráves do seu ID no banco de dados """
def AtualizarDadosPet(id_pet):

    petUpdate = request.get_json()

    try:
        petName = petUpdate['pet_name']
        idadePet = petUpdate['idade_pet']
        snVacinado = petUpdate['sn_vacinado']

        id = int(id_pet)

        if isinstance(id, int):
            updateData = update_pets(id_pet, petName, idadePet, bool(snVacinado))
            return updateData
        else:
            return jsonify({
                "message": "O parâmetro passado não é permitido!"
            }), 400

    except:
        return Response('''{"message": "Os dados não estão corretos!"}''', status=400, mimetype='application/json')

""" Pega soomente alguns dados do pet para usar em lookups """
def FiltroDePet():

    try:
        start = TimeExecute.StartTime()
        dadosFiltro = bancoSupabase.table("PETS").select("id_pets, pet_name, cd_pet, id_dono_pet(nm_cliente), tp_animal(raca)").execute()
        end = TimeExecute.EndTime()
        count = len(dadosFiltro.data)
        if count != 0:
            return jsonify({
                "filtro_pet": dadosFiltro.data,
                "message": f'{count} pets encontrados no banco!',
                "execute_time": f'Tempo de execução: {TimeExecute.MsgResultTime(end, start)} seconds'
            }), 201
        else:
            return jsonify({
                "message": "Nenhum pet foi encontrado no banco!"
            }), 400
    except:
        return Response('''{"message": "Algo deu errado na busca dos pets!"}''', status=400, mimetype='application/json')



