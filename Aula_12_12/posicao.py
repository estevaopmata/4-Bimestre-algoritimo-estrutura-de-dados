"""
faça uma lista com 10 lavores e motrar a posição onde se encontra o maior valor (sem utilizar funçoes prontas)
"""

valores = []


for i in range(10):   
    valoresunitaria = float(input("Digite os 10 numeros: "))  
    valores.append(valoresunitaria)

posicao = 0
for i in range(10):
    if valores [posicao] < valores[i]: #ele vai comprar posição por posição, na posição 0 vai ser atribuida o maior valor, depois compra na proxima posição, a posição 1, se o valor la dentro for menor entao a posição é substituida
        posicao = i
    
#agora que temos a posição onde esta o maior valor vamos ver que valor esta la dentro
print(f"Maior Valor: {valores[posicao]}")
print(f"posição do maior valor é: {posicao}")