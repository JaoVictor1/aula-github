#"id": 13,
#"titulo": "Retornando o Menor Número",
#"descricao": "Desenvolva uma função que receba uma lista de números e retorne o menor número encontrado nela."

def encontrar_menor(lista):
    return min(lista)

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Menor número:", encontrar_menor(numeros))