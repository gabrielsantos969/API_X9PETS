from email.errors import InvalidDateDefect
from flask import jsonify
from flask import request, Response
from BancoDeDados.store import bancoSupabase
from BancoDeDados.store import add_pets, update_pets

def PegarTodosPets():
    try:
        allPets = bancoSupabase.table("PETS").select("pet_name, idade_pet, sn_vacinado, sn_consulta, id_dono_pet(nm_cliente, celular_cliente, email_cliente, cpf_cliente), tp_animal(raca), especie_pet(ds_tp_especie)").execute()

        if len(allPets.data) != 0:
            return jsonify({
                'pets': allPets.data
            })
        else:
            return Response('''{"message": "Ainda não foi encontrado nenhum pet"}''', status=400, mimetype='application/json')

    except:
        return Response('''{"message": "Ainda não há animais cadastrados no sistema"}''', status=400, mimetype='application/json')


def BuscarPetPorId(pet_id):

    try:

        findPetId = bancoSupabase.table("PETS").select("pet_name, idade_pet, sn_vacinado, sn_consulta, id_dono_pet(nm_cliente, celular_cliente, email_cliente, cpf_cliente), tp_animal(raca), especie_pet(ds_tp_especie)").eq("id_pets", pet_id).execute()


        if len(findPetId.data) != 0:
            return jsonify({
                "filtro_id_pet": findPetId.data
            }), 201
        else:
            return Response('''{"message": "Este pet não está cadastrado em nosso sistema."}''', status=400, mimetype='application/json')
    except:
        return Response('''{"message": "Falha ao procurar rota"}''', status=400, mimetype='application/json')

def BuscarPetPorNome(name_pet):

    try:

        findPetName = bancoSupabase.table("PETS").select("pet_name, idade_pet, sn_vacinado, sn_consulta, id_dono_pet(nm_cliente, celular_cliente, email_cliente, cpf_cliente), tp_animal(raca), especie_pet(ds_tp_especie)").ilike("pet_name", str(f'%{name_pet}%')).execute()
        if len(findPetName.data) != 0:
            return jsonify({
                "filtro_name_pet": findPetName.data
            }), 201
        else:
            return Response('''{"message": "Nenhum pet com este nome encontrado"}''', status=400, mimetype='application/json')
    except:
        return Response('''{"message": "Algo deu errado"}''', status=400, mimetype='application/json')


def DeletarPet(id_pet):

    try:

        deletePet = bancoSupabase.table("PETS").delete().eq("id_pets", id_pet).execute()

        if len(deletePet.data) != 0:
            return jsonify(
                {
                    "message": "Pet exluido do banco de dados!",
                },
                {
                    "Dados apagados": deletePet.data
                }), 201
        else:
            return Response('''{"message": "O pet que deseja excluir não existe!"}''', status=400, mimetype='application/json')
    
    except:
        return Response('''{"message": "Algo deu errado em sua exclusão, verifique os dados!"}''', status=400, mimetype='application/json')


def CadastrarPet():
    data = request.get_json()

    try:
        petName = data['pet_name']
        tpAnimal = data['tp_animal']
        idDono = data['id_dono']

        if petName and tpAnimal and idDono:
            data = add_pets(petName, tpAnimal, int(idDono))
            return jsonify(data), 201
        else: 
            return Response('''{"message": "Os dados não foram encontrados!"}''', status=400, mimetype='application/json')
    except:
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')

def AtualizarDadosPet():

    petUpdate = request.get_json()

    try:
        petName = petUpdate['pet_name']
        idadePet = petUpdate['idade_pet']
        snVacinado = petUpdate['sn_vacinado']

        if petName and idadePet and snVacinado:
            updateData = update_pets(petName, idadePet, bool(snVacinado))

            return jsonify({
                "update_pet": updateData
            }), 201
        else:
            return Response('''{"message": "O pet não foi encontrado para atualizar!"}''', status=400, mimetype='application/json')

    except:
            return Response('''{"message": "Algo deu errado na atualização!"}''', status=400, mimetype='application/json')


