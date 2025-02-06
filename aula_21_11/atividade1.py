"""
Atividade 1
"""
numero1 = int(input("informe o primeiro numero: "))
numero2 = int(input("informe o segundo numero: "))
 
if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

print(f"O maior numero entre {maior} e {menor}o menor é : {menor}")