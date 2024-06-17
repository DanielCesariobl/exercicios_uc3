total = 0
vetor = []



#Entrada

while True:
    numero = float(input('Informe um numero: '))
    total = total + numero  
 #Processamento   
    if numero == 0:
     break
    else:
      vetor.append(numero)
#Saida
print('A quantidade de vetor é {}'.format (len(vetor)))
print('e o total é: {}'.format(total))
print('Utilizando a função sum {}'.format(sum(vetor)))

#vetor.pop() -  elimina a ultima posição do vetor, colocar fora do while