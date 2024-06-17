'''
1) Faça um programa que fará a leitura de indeterminados números e esses números serão armazenados em um vetor.
Quando o usuário digitar 0, 
o programa interromperá a leitura e irá imprimir o somatório dos números e a quantidade de elementos.

'''
total = 0
vetor = []
numero = -1


#Entrada
while True:
  try:  
    numero = float(input('Informe um numero: '))
    total = total + numero
    vetor.append(numero)
  except:
    print('Por favor, informe apenas números.') 
 #Processamento   
  if numero == 0:
    break
  
vetor.pop()
#Saida
print('A quantidade de vetor é {}'.format (len(vetor)))
print('e o total é: {}'.format(total))
print('Utilizando a função sum {}'.format(sum(vetor)))

#vetor.pop() -  elimina a ultima posição do vetor, colocar fora do while

    

