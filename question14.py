#"id": 14,
#"titulo": "Calculando a Média",
#"descricao": "Crie uma função que receba uma lista de números e retorne a média aritmética desses valores."

def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Média:", calcular_media(numeros))