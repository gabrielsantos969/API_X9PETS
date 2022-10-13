from flask import Flask, jsonify
from flask import Response
from Rotas import Animais, Clientes, Especie 
from dotenv import load_dotenv
load_dotenv()
import os

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
        "version": f'{os.getenv("VERSION")}',
        "status": f'{os.getenv("STATUS")}',
        "github": "https://github.com/Waichiro",
        "create at": "05/10/2022"
    })

""" =================================== ROTAS COM ACESSO A TABELA DE PETS NO BANCO DE DADOS ========================================= """

""" Rota para pegar todos os pets do banco de dados """
@app.route('/pets/all_pets', methods=['GET'])
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

""" Rota de filtro do pet OBS:(Trás menos dados que os outros) """
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

""" Rota para atualizacao de pet por ID """
@app.route('/pets/update/id=<id_pet>', methods=['POST'])
def update_pet(id_pet):
    return Animais.AtualizarDadosPet(id_pet)


""" ==================================   ROTAS DE ACESSO A TABELA DE CLIENTES ============================================"""

""" Puxa todos os clientes """
@app.route('/cliente/all_clients', methods=['GET'])
def all_clientes():
    return Clientes.PegarTodosClientes()

""" Filtro de busca de cliente por ID """
@app.route('/cliente/id=<id_cliente>')
def cliente_find_by_id(id_cliente):
    return Clientes.BuscarClientesPorId(id_cliente)

""" ==================================== ROTAS DE ESPECIE ==================================================== """
""" Rota para a busca de todos as especies """
@app.route('/especies/all_especies', methods=['GET'])
def all_especies():
    return Especie.TodasEspecies()

""" Rota de cadastastro de especie """
@app.route('/especie/add', methods=['POST'])
def add_especie():
    return Especie.CadastrarEspecie()

""" Rota para atualizacao de especie """
@app.route('/especie/update/id=<id_especie>', methods=['POST'])
def update_especie(id_especie):
    return Especie.AtualizarDadosEspecie(id_especie)

@app.route('/especie/name=<nm_especie>', methods=['GET'])
def findEspecieByName(nm_especie):
    return Especie.BuscarEspeciePorNome(nm_especie)

""" CORS PARA PUXAR DADOS DA API """
@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers","Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods","*")
    response.headers.add("Access-Control-Max-Age","86400")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

