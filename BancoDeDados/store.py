from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client, Client


url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def add_pets(pet_name, tp_animal, id_dono) -> dict:
    pets= {
        "pet_name": pet_name,
        "tp_animal": tp_animal,
        "id_dono": id_dono
    }

    data = supabase.table("pets").insert(pets).execute()

    return   data.data

def update_pets(pet_name, idade_pet, sn_vacina):
    updatePet = {
        "pet_name": pet_name,
        "idade_pet": idade_pet,
        "sn_vacinado": sn_vacina
    }
    updateData = supabase.table("PETS").update(updatePet).execute()

    return updateData.data

bancoSupabase = supabase
