from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

# Criando a conexão com o banco de dados SQLite (substitua 'sqlite:///teste.db' pelo caminho desejado)
engine = create_engine('sqlite:///teste.db', echo=True)

# Criando uma instância da classe declarative_base
Base = declarative_base()

# Definindo a classe Cliente
class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    endereco = Column(String)

    contas = relationship('Conta', back_populates='cliente')

# Definindo a classe Conta
class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Float)

    cliente = relationship('Cliente', back_populates='contas')

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criando uma sessão para interagir com o banco de dados
session = Session(engine)

# Inserindo dados mínimos
cliente1 = Cliente(nome='João da Silva', cpf='123.456.789-00', endereco='Rua A, 123')
cliente2 = Cliente(nome='Maria Oliveira', cpf='987.654.321-00', endereco='Rua B, 456')

conta1 = Conta(tipo='Corrente', agencia='001', num=1234, saldo=1000.0)
conta2 = Conta(tipo='Poupança', agencia='002', num=5678, saldo=500.0)

# Associando contas aos clientes
cliente1.contas.append(conta1)
cliente2.contas.append(conta2)

# Adicionando os objetos à sessão
session.add_all([cliente1, cliente2])

# Commit para efetivar as alterações no banco de dados
session.commit()

# Recuperando dados
clientes = session.query(Cliente).all()
contas = session.query(Conta).all()

# Exibindo dados recuperados
print("Clientes:")
for cliente in clientes:
    print(f"ID: {cliente.id}, Nome: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}")

print("\nContas:")
for conta in contas:
    print(f"ID: {conta.id}, Tipo: {conta.tipo}, Agência: {conta.agencia}, Número: {conta.num}, Saldo: {conta.saldo}")

# Fechando a sessão
session.close()