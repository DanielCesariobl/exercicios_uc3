'''
escreva um algoritimo que leia um numero,
o programa calcule e exibira a tabuada deste numero.
mostre a tabuada na forma 


'''

numero = int(input('Informe um numero'))
for i in range(1,11):
 r = numero * i

 print (f'{i} x {numero} = {r}')

   