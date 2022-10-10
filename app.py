from flask import Flask, jsonify
from flask import Response
from Rotas import Animais, Clientes 

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return Response('''{"message": "Está rota não existe"}''', status=404, mimetype='application/json')

""" Rota inicial da API """
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "greeting": "Welcome to API ",
        "developer": "Gabriel Santos",
        "version": "1.0.1",
        "github": "https://github.com/Waichiro",
        "create at": "05/10/2022"
    })

""" =================================== ROTAS COM ACESSO A TABELA DE PETS NO BANCO DE DADOS ========================================= """

""" Rota para pegar todos os pets do banco de dados """
@app.route('/all_pets', methods=['GET'])
def all_pets():
    return Animais.PegarTodosPets()

""" =================================== ROTAS DE FILTRO DA TABELA DE PETS =========================================== """

""" Rota para procurar pet pelo seu ID """
@app.route('/pets/id=<pet_id>', methods=['GET'])
def find_pet_by_id(pet_id):
    return Animais.BuscarPetPorId(pet_id)
    

""" Procurar pet pelo nome """
@app.route('/pets/name=<name_pet>', methods=['GET'])
def find_pet_by_name(name_pet):
    return Animais.BuscarPetPorNome(name_pet)

@app.route('/pets/filtro_pets', methods=['GET'])
def filtro_pets():
    return Animais.FiltroDePet()

""" ================================================ ROTAS DE POST DA TABELA DE PETS ======================================== """

""" Rota para adicionar um novo pet por JSON """
@app.route('/pets/add', methods=['POST'])
def add_pet():
    return Animais.CadastrarPet()


""" Rota para deletar um pet pelo seu ID """
@app.route('/pets/delete/id=<id_pet>', methods=['POST'])
def delete_pet(id_pet):
    return Animais.DeletarPet(id_pet)


@app.route('/pets/update/id=<id_pet>', methods=['POST'])
def update_pet(id_pet):
    return Animais.AtualizarDadosPet(id_pet)


""" ==================================   ROTAS DE ACESSO A TABELA DE CLIENTES ============================================"""

""" Puxa todos os clientes """
@app.route('/all_clients', methods=['GET'])
def all_clientes():
    return Clientes.PegarTodosClientes()

@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers","Content-Type,Authorization")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)