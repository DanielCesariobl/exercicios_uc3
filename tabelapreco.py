'''
4) O cardápio de uma lanchonete é o seguinte:

Especificação   Código      Preço
Cachorro quente  100         1,20
Bauru simples    101          1,30
Bauru com ovo    102          1,50
Hambúrge         103         1,20
Cheeseburguer    104        1,30
Refrigerante     105          1,00
Escrever um algoritmo que leia o código do item pedido, a quantidade e 
calcule o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um item.


'''
codigo = int(input("Digite o codigo do produto:  "))
quantidade = int(input('Digite a quantidade: '))

if codigo == 100:
  print('o valor é {:.2f}'.format(quantidade * 1.20))

elif codigo == 101:
    print ('o valor é {:.2f}'.format(quantidade * 1.30))  

elif codigo == 102:
    print ('o valor é {:.2f}'.format(quantidade * 1.50))  

elif codigo == 103:
    print ('o valor é {:.2f}'.format(quantidade * 1.20))  

elif codigo == 104:
    print ('o valor é {:.2f}'.format(quantidade * 1.30))  

elif codigo == 105:
    print ('o valor é {:.2f}'.format(quantidade * 1.00))  

    