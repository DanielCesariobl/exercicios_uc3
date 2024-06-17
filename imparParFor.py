'''
faça um programa que peça 10 numeros inteiros, calcule e mostre 
a quantidade de numeros pares e a quantidade de numeros impares

'''
par = 0
impar = 0
for numero in range (10):
    n = int(input('Informe um numero'))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1   

print(f'numero de pares: {par}')       
print(f'numeros impares:{impar}')