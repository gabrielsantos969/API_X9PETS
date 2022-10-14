# API do sistema X9pets V.1.1.3

> Status do Projeto: Em desenvolvimento :warning:

API do sistema X9pets, a API é para a conexão com o banco de dados e a busca de dados e envio de dados.

### Detalhes
- [X] Conexão com o Banco de dados
- [X] Error 404 em rotas
- [X] Busca de todos os Animais
- [X] Update de Animais
- [X] Delete de Animais
- [X] Busca por ID do Animal
- [X] Busca por NOME do Animal
- [X] Cadastro dos Animais
- [X] Buscar todas especies
- [X] Cadastro das especies
- [ ] Deleta especies
- [X] Atualiza especies
- [ ] Busca de todos os Clientes
- [ ] Update de Clientes
- [ ] Cadastro de Clientes
- [ ] Busca por NOME do Cliente
- [X] Busca por ID de Cliente
- [ ] Busca de todos os Clientes
- [ ] Busca por ID de Funcionario
- [ ] Busca de todos os Funcionarios
- [ ] Busca por NOME de Funcionario
- [ ] Update por ID de Funcionario
- [ ] Delete por ID de Funcionario
- [ ] Autenticação para acesso a banco de dados

## Atualizações
- V1.1.1: 
    - Adicionado o update de dados dos pets.
    - Puxando mais dados do banco na busca do pet tanto por ID quanto por NOME e na busca de todos os pets.
    - Adicionado a rota de update.
    - Adicionado a função para update no store.
- V1.1.2:
    - Adicionado funções de API para facilitar em processos repetitivos no código.
    - Filtro para lista simples de animais cadastrados.
    - Adicionado mensagens de retorno de cada função executada.
    - Adicionado tempo de execução de cada função executa no banco de dados. 
    - Adicionado rotas de todas as especies, de cadastrar especie e de atualizar especies.
    - Adicionado novo arquiva para Funções de ESPECIE.
    - Adicionado busca de cliente por ID.
    - Ajustado função de API para trazer frase no return do resultExecute.
- 1.1.3(Em desenvolvimento):
    - Autenticação do banco de dados para acessar os dados(Em produção).
    - Busca de especie por nome.
# Como rodar a aplicação:

### No terminal clone o projeto:
    git clone https://github.com/Waichiro/API_X9PETS 

### Entre na pasta do projeto:

    cd API_X9PETS
### Instale as dependencias:

    pip install -r requirements.txt

### Execute a aplicação:

    flask run

### Agora você pode acessar o projeto na rota (http://localhost:5000)

## Deploy da Aplicação com Heroku: :dash:

> https://x9pets-api.herokuapp.com/

### Participantes: 
|Nome|Email|Presente|Função|Curso|
| -------- | -------- | -------- |-------- | -------- |
|Gabriel Santos|americaezo1@gmail.com|Sim|Back-End|Ciências da Computação|


[<img src="https://github.com/Waichiro.png" width=115 > <br> <sub> Gabriel Santos </sub>](https://github.com/Waichiro) |
| :---: |  