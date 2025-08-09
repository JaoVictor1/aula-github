#"id": 2,
#"titulo": "Encontrando o Maior Número",
#"descricao": "Escreva uma função que receba uma lista de números e retorne o maior número encontrado nela."

def encontrar_maior(lista):
    # Caso base: se a lista tiver só um elemento, ele é o maior
    if len(lista) == 1:
        return lista[0]
    else:
        # Compara o primeiro elemento com o maior do resto da lista
        maior_do_resto = encontrar_maior(lista[1:])
        return lista[0] if lista[0] > maior_do_resto else maior_do_resto

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
print("Maior número:", encontrar_maior(numeros))