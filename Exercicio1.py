


valorTotal = float(input('Informe o valor total da compra '))
numeroParcelas = int(input('Informe a quantidade de parcelas'))

valorCartao = valorTotal / numeroParcelas

# print (f'O valor que irá pagar no més é: {valorCartao:.2f}')
print("Você parcelou em {} no cartão e ficou no total de {:.2f} ".format(numeroParcelas, valorCartao))