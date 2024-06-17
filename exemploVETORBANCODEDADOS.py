agenda = []

nome =input('Informe seu nome: ')
idade = int(input('Informe sua idade ')) 
email  = input('infome seu email: ')
endereco = input('Informe seu endereço')
telefone = input('Informe seu numero')

agenda.append([nome,idade,email,endereco,telefone]) 
agenda.append(['Maria',30,'Maria@teste','teste', '222'])
print(agenda)

print(agenda [0])

#Nome
print(agenda[0][0])
print (agenda[1][0])