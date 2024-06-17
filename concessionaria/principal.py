'''
Uma concessionária necessita de um programa que fará o cadastro de automóveis que serão comercializados pela mesma.
Cada veículo possui os seguintes campos: Nome, ano, valor, descrição, e se Okm ou usado.
Faça a leitura dos automóveis até o usuário decidir não continuar com a leitura.
Ao terminar a leitura, o programa deverá listar todos os veículos cadastrados.
'''
from funcoes import cadastrar, cadastrarCliente,cadastrarMarca, excluirCliente, excluirVeiculos, listarCliente, listarMarca, listarVeiculos
agenda = []

while True:
    print('='*28)
    print(' Bem vindo à Concessionária')
    print('='*28)
    print('1 - Cadastrar Veículos ')
    print('2 - Listar Veículos ')
    print('3 - Excluir Veiculo  ')
    print('4 - Cadastrar Marcas ')
    print('5 - Listar Marcas ')
    print('6 - Adicionar Cliente ')
    print('7 - Listar Cliente ')
    print('8 - Excluir Cliente ')
    print('0 - Sair ')  
    print('='*25)
    try:      
     opcao = int(input('Digite opção desejada  '))
     match(opcao):
        case 1:
            cadastrar(agenda)
        case 2:
            listarVeiculos()
        case 3:    
             excluirVeiculos()
        case 4:
            cadastrarMarca()
        case 5:
            listarMarca()    
        case 6:
             cadastrarCliente()    
        case 7:
             listarCliente()     
        case 8:
             excluirCliente()    
        case 0:
            print('Até a próxima')    
            break  
        case _:
            print('Opção Invalida')    
    except:
        print('erro na seleção de opção')
        
    