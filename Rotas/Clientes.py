from BancoDeDados.store import bancoSupabase
from flask import jsonify
from flask import Response


def PegarTodosClientes():
    try:
        all_clients = bancoSupabase.table("CLIENTE").select("nm_cliente, celular_cliente, email_cliente, cidade_cliente(nm_cidade, uf)").execute()

        if len(all_clients.data) != 0:
            return jsonify({
                "all_clients": all_clients.data
            })
        else:
            return Response('''{"message": "Ainda não há nenhum cliente cadastrado no sistema"}''', status=400, mimetype='application/json')

    except:
        return Response('''{"message": "Parece que algo deu errado na busca de clientes!"}''', status=400, mimetype='application/json')

            