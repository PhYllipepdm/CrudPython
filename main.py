#Sistema para Cadastro de Clientes
import os
import sqlite3

conexao = sqlite3.connect('cliente.db')
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        numero TEXT NOT NULL
    )
''')
conexao.commit()
conexao.close()

def cadastrar_cliente():
  os.system('clear') 
  
  nome = input("\nDigite o nome do cliente: ").upper()
  endereco = input("\nDigite o endereco: ").lower()
  numero = input("\nDigite o número do cliente: ")
  
  conexao = sqlite3.connect('cliente.db')
  cursor = conexao.cursor()

  cursor.execute(
    'INSERT INTO cliente (nome,endereco,numero) VALUES(?,?,?)',(nome,endereco,numero))

  conexao.commit()
  conexao.close()

def lista_clientes():
  os.system('clear')
  conexao = sqlite3.connect('cliente.db')
  cursor = conexao.cursor()

  cursor.execute('SELECT * FROM cliente')
  clientes = cursor.fetchall()

  for cliente in clientes:
    print(f'\nID: {cliente[0]}, '
          f'Nome: {cliente[1]}, '
          f'Endereço: {cliente[2]}, '
          f'Número: {cliente[3]}\n')

  conexao.close()

def verificar_nome(nome_cliente):
  conexao = sqlite3.connect('cliente.db')
  cursor = conexao.cursor()

  cursor.execute("SELECT * FROM cliente WHERE nome = ?", (nome_cliente,))
  return cursor.fetchone() 


def atualizar_cliente():
  os.system('clear')
  conexao = sqlite3.connect('cliente.db')
  cursor = conexao.cursor()
  
  nome_cliente = input("Digite o nome do cliente que deseja Alterar: ").upper()
  
  if verificar_nome(nome_cliente):
    novo_nome = input("\nDigite o nome do cliente: ").upper()
    novo_endereco = input("\nDigite o novo endereco: ").lower()
    novo_numero = input("\nDigite o novo número do cliente: ")
    
    cursor.execute("UPDATE cliente SET nome = ?, endereco= ?, numero= ? WHERE nome= ?", 
      (novo_nome, novo_endereco, novo_numero, nome_cliente))
    conexao.commit()
    print("\nCliente Alterado com sucesso!")

  else:
    print(f"O cliente {nome_cliente} não está cadastrado na base de dados")


def deletar_cliente():
  os.system('clear')
  id_cliente = input("Digite o ID do cliente que deseja deletar: ")
  
  conexao = sqlite3.connect('cliente.db')
  cursor = conexao.cursor()

  cursor.execute("DELETE FROM cliente WHERE id = ?", (id_cliente))
  conexao.commit()
  print("\nCliente deletado com sucesso.")

  # Renumerar os IDs após a exclusão
  cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=SEQ-1 WHERE NAME='cliente'")
  conexao.commit()
  
def main():
  escolha = '0'
  while escolha != '5':
    print('\n1 - CADASTRO\n2 - LISTAR\n3 - ATUALIZAR\n4 - DELETAR\n5 - SAIR')
  
    escolha = input("\nEscolha uma das opções acima: ")
  
    if escolha == '1':
      cadastrar_cliente()
    elif escolha == '2':
      lista_clientes()
    elif escolha == '3':
      atualizar_cliente()
    elif escolha == '4':
      deletar_cliente()
    elif escolha > '5' or escolha < '0':
      print('Opção Inválida')
    
main()