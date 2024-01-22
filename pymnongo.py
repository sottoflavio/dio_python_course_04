from pymongo import MongoClient

# Conectar ao MongoDB Atlas (substitua 'SEU_CONNECTION_STRING' pelo URL fornecido pelo MongoDB Atlas)
client = MongoClient('SEU_CONNECTION_STRING')

# Criar ou acessar o banco de dados
db = client['seu_banco_de_dados']

# Definir uma coleção chamada 'bank' para armazenar documentos de clientes
collection = db['bank']

# Inserir documentos com a estrutura mencionada
cliente1 = {
    "id": 1,
    "nome": "João da Silva",
    "cpf": "123.456.789-00",
    "endereco": "Rua A, 123",
    "contas": [
        {"id": 1, "tipo": "Corrente", "agencia": "001", "num": 1234, "saldo": 1000.0},
        {"id": 2, "tipo": "Poupança", "agencia": "002", "num": 5678, "saldo": 500.0}
    ]
}

cliente2 = {
    "id": 2,
    "nome": "Maria Oliveira",
    "cpf": "987.654.321-00",
    "endereco": "Rua B, 456",
    "contas": [
        {"id": 3, "tipo": "Corrente", "agencia": "003", "num": 9876, "saldo": 1500.0}
    ]
}

# Inserir os documentos na coleção
collection.insert_many([cliente1, cliente2])

# Recuperar informações com base em pares de chave e valor
# Exemplo: Recuperar todas as informações de um cliente com CPF específico
cpf_procurado = "123.456.789-00"
cliente_encontrado = collection.find_one({"cpf": cpf_procurado})
print(f"Informações do cliente com CPF {cpf_procurado}:")
print(cliente_encontrado)

# Exemplo: Recuperar todas as contas de um cliente com base no nome
nome_procurado = "João da Silva"
contas_do_cliente = collection.find_one({"nome": nome_procurado}, {"contas": 1})
print(f"Contas do cliente {nome_procurado}:")
print(contas_do_cliente.get("contas", []))

# Fechar a conexão com o MongoDB Atlas
client.close()