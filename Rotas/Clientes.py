from BancoDeDados.store import bancoSupabase
from FuncoesDeAPI import TimeExecute
from flask import jsonify
from flask import Response

""" =========================================== BUSCA AO BANCO DE DADOS ======================================== """
""" Função que pega todos os clientes """
def PegarTodosClientes():
    try:
        start = TimeExecute.StartTime()
        all_clients = bancoSupabase.table("CLIENTE").select("nm_cliente, celular_cliente, email_cliente, cidade_cliente(nm_cidade, uf)").execute()
        end = TimeExecute.EndTime()
        count = len(all_clients.data)

        if count != 0:
            return jsonify({
                "all_clients": all_clients.data,
                "message": f'Foram encontrados {count} clientes.',
                "time_execute": f'{TimeExecute.MsgResultTime(end, start)}'
            })
        else:
            return Response('''{"message": "Ainda não há nenhum cliente cadastrado no sistema"}''', status=400, mimetype='application/json')

    except:
        return Response('''{"message": "Parece que algo deu errado na busca de clientes!"}''', status=400, mimetype='application/json')


""" ================================ FUNÇÃO DE FILTRO PARA BUSCA NO BANCO ======================================== """
""" Busca o cliente por ID """
def BuscarClientesPorId(id_cliente):
    try:

        start =  TimeExecute.StartTime()
        clienteId = bancoSupabase.table("CLIENTE").select("nm_cliente, celular_cliente, email_cliente, cidade_cliente(nm_cidade, uf)").eq("id_cliente", id_cliente).execute()
        end = TimeExecute.EndTime()
        count = len(clienteId.data)

        if count != 0:
            return jsonify({
                "cliente": clienteId.data,
                "message": f'{count} cliente(s) encontrado(s).',
                "time_execute": f'{TimeExecute.MsgResultTime(end, start)}'
            }), 201
        else:
            return jsonify({
                "message": "Nenhum cliente encontrado!"
            }), 400

    except:
        return Response('''{"message": "Parece que algo deu errado na busca de clientes!"}''', status=400, mimetype='application/json')
            