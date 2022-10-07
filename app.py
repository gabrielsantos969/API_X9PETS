from flask import Flask, jsonify
from flask import request, Response
from store import bancoSupabase
from store import add_pets

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'greeting': 'Hello World!'
    })

""" Rota para pegar todos os pets do banco de dados """
@app.route('/pets')
def pegarPets():
    data = bancoSupabase.table("pets").select("*").execute()

    return jsonify({
        'pets2': data.data
    })

""" Rota para procurar pet pelo seu ID """
@app.route('/pets/<pet_id>')
def find_pet_by_id(pet_id):
    data = bancoSupabase.table("pets").select("*").eq("id", pet_id).execute()

    return data.data

@app.route('/pets/<str:name_pet>')
def find_pet_by_name(name_pet):
    data = bancoSupabase.table("pets").select("*").eq("pet_name", str(name_pet)).execute()

    return data.data

""" Rota para adicionar um novo pet por JSON """
@app.route('/pets/add', methods=['POST'])
def add_pet():
    data = request.get_json()

    try:
        petName = data['pet_name']
        tpAnimal = data['tp_animal']
        idDono = data['id_dono']

        if petName and tpAnimal and idDono:
            data = add_pets(petName, tpAnimal, int(idDono))
            return jsonify(data), 201
    except:
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')

""" Rota para deletar um pet pelo seu ID """
@app.route('/pets/delete/<id_pet>')
def delete_pet(id_pet):
    data = bancoSupabase.table("pets").delete().eq("id", id_pet).execute()
    return data.data

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)