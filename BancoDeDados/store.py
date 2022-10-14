
from dotenv import load_dotenv
load_dotenv()
import os
from FuncoesDeAPI import TimeExecute
from flask import Response, jsonify
from supabase import create_client, Client


url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

""" Função para cadastro de PET """
def add_pets(pet_name, tp_animal, id_dono, cd_pet, tp_especie) -> dict:
    pets= {
        "pet_name": pet_name,
        "tp_animal": tp_animal,
        "id_dono_pet": id_dono,
        "cd_pet": cd_pet,
        "especie_pet": tp_especie
    }
    start = TimeExecute.StartTime()
    dadosCadastro = supabase.table("PETS").insert(pets).execute()
    end = TimeExecute.EndTime()

    return jsonify({
        "dados": dadosCadastro.data,
        "message": "Pet cadastrado com sucesso!",
        'time_execute': f'{TimeExecute.MsgResultTime(end, start)}'
    })

""" Função para atualização de PET """
def update_pets(id_pet, pet_name, idade_pet, sn_vacina):
    updatePet = {
        "pet_name": pet_name,
        "idade_pet": idade_pet,
        "sn_vacinado": sn_vacina
    }
    start = TimeExecute.StartTime()
    data = supabase.table("PETS").select("id_pets").eq("id_pets", int(id_pet)).execute()
    end = TimeExecute.EndTime()
    count = len(data.data)
    if count != 0:
        
        updateData = supabase.table("PETS").update(updatePet).eq("id_pets", int(id_pet)).execute()

        return jsonify({
           "dados": updateData.data,
           "message": "Dados atualizados!" ,
           'time_execute': f'{TimeExecute.MsgResultTime(end, start)}'
        }), 201
    elif count == 0:
        return jsonify({
            "message": "O ID não existe no banco de dados!"
        }), 400

    elif isinstance(id_pet, str):
        return jsonify({
            "message": "O ID não pode ser uma string!"
        }), 400

""" Função para cadastro de ESPECIE """
def add_especie(nmEspecie, cdEspecie) -> dict:
    especie= {
        "ds_tp_especie": nmEspecie,
        "cd_tp_especie": cdEspecie,

    }
    start = TimeExecute.StartTime()
    dadosCadastro = supabase.table("TP_ESPECIE").insert(especie).execute()
    end = TimeExecute.EndTime()

    return jsonify({
        "dados": dadosCadastro.data,
        "message": "Especie cadastrada com sucesso!",
        'time_execute': f'{TimeExecute.MsgResultTime(end, start)}'
    })

""" Função para atualização de ESPECIE """
def update_especie(id_especie, especie_name):
    updateEspecie = {
        "ds_tp_especie": especie_name
    }
    start = TimeExecute.StartTime()
    data = supabase.table("TP_ESPECIE").select("id_tp_especie").eq("id_tp_especie", int(id_especie)).execute()
    end = TimeExecute.EndTime()
    count = len(data.data)
    print(count)
    if count != 0:
        
        updateData = supabase.table("TP_ESPECIE").update(updateEspecie).eq("id_tp_especie", int(id_especie)).execute()

        return jsonify({
           "dados": updateData.data,
           "message": "Dados atualizados!" ,
           'time_execute': f'{TimeExecute.MsgResultTime(end, start)}'
        }), 201
    elif count == 0:
        return jsonify({
            "message": "O ID não existe no banco de dados!"
        }), 400
    else:
        return jsonify({
            "message": "O ID não pode ser uma string!"
        }), 400


bancoSupabase = supabase
