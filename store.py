from dotenv import load_dotenv
import json

load_dotenv()
import os
import requests
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

bancoSupabase = supabase
