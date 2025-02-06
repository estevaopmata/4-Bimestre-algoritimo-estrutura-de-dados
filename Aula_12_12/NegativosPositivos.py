"""
Vamos fazer um programa que leia 10 numeros reais e os armazene em uma lista. calcule e mostra a quantidade de numeros negativos a soma dos numeros positivos
"""

numero = []

soma_positivos = 0
quantidade_negativos = 0

for i in range(10):   
    numerounitaria = float(input("Digite os numeros: "))  
    numero.append(numerounitaria) 
  
for numerounitaria in numero:
    if numerounitaria < 0:
        quantidade_negativos += 1  
    if numerounitaria > 0:
        soma_positivos += numerounitaria
        
print (f"Quantidade de Negativos: {quantidade_negativos}\nSoma dos Positivos: {soma_positivos}")   

