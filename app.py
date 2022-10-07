from flask import Flask, jsonify
from flask import request, Response
from store import bancoSupabase
from store import add_pets

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return Response('''{"message": "Está rota não existe"}''', status=404, mimetype='application/json')

""" Rota inicial da API """
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'greeting': 'Hello World!'
    })

""" Rota para pegar todos os pets do banco de dados """
@app.route('/pets', methods=['GET'])
def pegarPets():

    try:
        data = bancoSupabase.table("PETS").select("pet_name, id_dono_pet(nm_cliente, celular_cliente, email_cliente), tp_animal(raca)").execute()

        if len(data.data) != 0:
            return jsonify({
                'pets': data.data
            })
    except:
        return Response('''{"message": "Ainda não há animais cadastrados no sistema"}''', status=400, mimetype='application/json')

""" Rota para procurar pet pelo seu ID """
@app.route('/pets/id=<pet_id>', methods=['GET'])
def find_pet_by_id(pet_id):

    try:

        data = bancoSupabase.table("PETS").select("pet_name, id_dono_pet(nm_cliente, celular_cliente, email_cliente), tp_animal(raca)").eq("id_pets", pet_id).execute()


        if len(data.data) != 0:
            return jsonify({
                "filtro_id_pet": data.data
            }), 201
        else:
            return Response('''{"message": "Este pet não está cadastrado em nosso sistema."}''', status=400, mimetype='application/json')
    except:
        return Response('''{"message": "Falha ao procurar rota"}''', status=400, mimetype='application/json')
    

""" Procurar pet pelo nome """
@app.route('/pets/name=<name_pet>', methods=['GET'])
def find_pet_by_name(name_pet):

    try:

        data = bancoSupabase.table("PETS").select("pet_name, id_dono_pet(nm_cliente, celular_cliente, email_cliente), tp_animal(raca)").ilike("pet_name", str(f'%{name_pet}%')).execute()
        if len(data.data) != 0:
            return jsonify({
                "filtro_name_pet": data.data
            }), 201
        else:
            return Response('''{"message": "Nenhum pet com este nome encontrado"}''', status=400, mimetype='application/json')
    except:
        return Response('''{"message": "Algo deu errado"}''', status=400, mimetype='application/json')


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
        else: 
            return Response('''{"message": "Os dados não foram encontrados!"}''', status=400, mimetype='application/json')
    except:
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')


""" Rota para deletar um pet pelo seu ID """
@app.route('/pets/delete/id=<id_pet>', methods=['POST'])
def delete_pet(id_pet):

    try:

        data = bancoSupabase.table("PETS").delete().eq("id_pets", id_pet).execute()

        if len(data.data) != 0:
            return data.data, 201
        else:
            return Response('''{"message": "O pet que deseja excluir não existe!"}''', status=400, mimetype='application/json')
    
    except:
        return Response('''{"message": "Algo deu errado em sua exclusão, verifique os dados!"}''', status=400, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)