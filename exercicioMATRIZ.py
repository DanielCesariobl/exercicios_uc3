'''
2) Completar o programa, fazendo a leitura em um loop, e sempre perguntando se o usuário deseja continuar cadastrando
Ao encerrar a leitura, exibir as pessoas que são menores de idade.

'''
agenda = []
resp =''

while True:
    nome =input('Informe seu nome: ')
    idade = int(input('Informe sua idade ')) 
    email  = input('infome seu email: ')
    endereco = input('Informe seu endereço')
    telefone = input('Informe seu numero')

    agenda.append([nome,idade,email,endereco,telefone]) 
    resp = input('deseja continuar (s/n)').lower()
    if resp =='n':
       break
    
for contato in agenda:
    if contato[1] <= 18:
        print(contato)



    '''
    if idade >18:
     print('os maiores de idade são {}'.format(agenda)) 
    else:
     print('os menores de idades são{}'.format(agenda))  
     '''
  
 
    
