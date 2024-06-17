
from conexao import conectar
def cadastrar(agenda):
    while True:
        carros = {}
        carros['nome']  = input('Informe nome do carro: ')
        carros['valor'] = float(input('Informe o valor do carro: '))
        carros['ano'] = int(input('informe o ano do carro: '))
        carros['descricao'] = input('Informe a descrição do carro: ')
        carros['usado'] =input('Informe se o carro e 0km ou usado: ')
        

        con = conectar()
        cursor = con.cursor()
        sql = 'insert into veiculo (nome, valor, descricao, tipo) values (%s,%s,%s,%s)'
        cursor.execute(sql,(carros['nome'],carros['valor'],carros['descricao'],carros['usado']))
        con.commit()
        r = input('Deseja continuar (s/n) ? ').lower()
        if r =='n':
            break

def listar(agenda):            
    for contato in agenda:
        print(f"Nome:  {contato['nome']}\nValor:  {contato['valor']}\nAno:  {contato['ano']}\nDescrição:  {contato['descricao']}\nNovo ou Usado:  {contato['usado']}")
        print('_'*50)

def cadastrarMarca():
    while True:
        marca = {}
        marca['marca'] = input('Informe a marca do carro:  ')
        con = conectar()
        cursor = con.cursor()

        sql = 'insert into marca (nome) values (%s)'
        cursor.execute(sql,(marca['marca'],))
        con.commit()

        r = input('Deseja continuar (s/n) ? ').lower()
        if r =='n':
            break

def listarVeiculos():
    con = conectar()
    cursor = con.cursor()
    sql = 'select * from veiculo order by nome'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for v in resultado:
       print('='*30)
       print(v)
       
def listarMarca():
    con = conectar()
    cursor = con.cursor()
    sql = 'select * from marca order by nome'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for m in resultado:
        print(m)

def cadastrarCliente():
    while True:
        cliente = {}
        cliente['nome']  = input('Informe nome do cliente: ')
        cliente['cpf'] = (input('Informe o cpf do cliente: '))
        cliente['endereco'] = (input('informe endereço do cliente: '))
        cliente['telefone'] = (input('Informe o telefone do cliente: '))

        con = conectar()
        cursor = con.cursor()
        sql = 'insert into cliente (nome, cpf, endereco, telefone) values (%s,%s,%s,%s)'
        cursor.execute(sql,(cliente['nome'],cliente['cpf'],cliente['endereco'],cliente['telefone']))
        con.commit()
    
        r = input('Deseja continuar (s/n) ? ').lower()
        if r =='n':
         break
        
def listarCliente():
    con = conectar()
    cursor = con.cursor()
    sql = 'select * from cliente order by nome'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for c in resultado:
        print(c)
    
        
def excluirCliente():
    try:
        conexao = conectar()
        cursor = conexao.cursor()    
        id_para_excluir = input("Digite o ID que deseja excluir: ")
        sql = f"DELETE FROM cliente WHERE id = {id_para_excluir}"
        cursor.execute(sql)
        conexao.commit()
        print(f"Registro com ID {id_para_excluir} excluído com sucesso!")
    except:
        print(f"Erro ao excluir registro:")
    
    '''
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão encerrada.")
    '''

def excluirVeiculos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()    
        id_para_excluir = input("Digite o ID que deseja excluir: ")
        sql = f"DELETE FROM veiculo WHERE id = {id_para_excluir}"
        cursor.execute(sql)
        conexao.commit()
        print(f"Registro com ID {id_para_excluir} excluído com sucesso!")
    except:
        print(f"Erro ao excluir registro:")
    


        














'''
def listar (agenda)
  for c in agenda:
  for k, v in c.items():
  print(f'{k}: {v}')
  print('_'*50) 
'''