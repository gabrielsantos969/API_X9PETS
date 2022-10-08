from dotenv import load_dotenv
load_dotenv()
import os
from flask import Response, jsonify
from supabase import create_client, Client


url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def add_pets(pet_name, tp_animal, id_dono, cd_pet, tp_especie) -> dict:
    pets= {
        "pet_name": pet_name,
        "tp_animal": tp_animal,
        "id_dono_pet": id_dono,
        "cd_pet": cd_pet,
        "especie_pet": tp_especie
    }
    print("Opa")
    dadosCadastro = supabase.table("PETS").insert(pets).execute()
    print(dadosCadastro.data)
    return jsonify({
        "dados": dadosCadastro.data,
        "message": "Pet cadastrado com sucesso!"
    })

def update_pets(id_pet, pet_name, idade_pet, sn_vacina):
    updatePet = {
        "pet_name": pet_name,
        "idade_pet": idade_pet,
        "sn_vacinado": sn_vacina
    }

    data = supabase.table("PETS").select("id_pets").eq("id_pets", int(id_pet)).execute()

    if len(data.data) != 0:
        
        updateData = supabase.table("PETS").update(updatePet).eq("id_pets", int(id_pet)).execute()

        return jsonify({
           "dados": updateData.data,
           "message": "Dados atualizados!" 
        }), 201
    elif isinstance(id_pet, str):
        print("Entrei")
        return jsonify({
            "message": "O ID não pode ser uma string!"
        }), 400


bancoSupabase = supabase
