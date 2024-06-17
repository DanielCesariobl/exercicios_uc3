#vetor - conjunto - array - lista

vetor =[] #declarando vetor
vetor.append ('luis') #adicionadno elemetnesos
vetor.append('renato')
vetor.append('pedro')
print(vetor)
print(vetor[0])  # 0 e a primeira posição do vetor

vetor.append(input('informe o  nome:'))
print(vetor)

print(len(vetor)) # 'len' retorna o numero de elementos de um vetor

for nome in vetor:
    print(nome)
