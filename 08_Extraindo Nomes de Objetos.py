#"id": 7,
#"titulo": "Extraindo Nomes de Objetos",
#"descricao": "Crie uma função que receba uma lista de objetos (onde cada objeto tem um atributo 'nome') e retorne uma nova lista contendo apenas os nomes de cada objeto."

def extrair_nomes(lista):
    nomes_salvos = []

    # Para cada objeto na lista
    for obj in lista:
        # Acessa o valor do campo "nome"
        nomes_salvos.append(obj["nome"])

    return nomes_salvos


pessoas = [
    {"nome": "João"},
    {"nome": "Larissa"},
    {"nome": "Clara"},
    {"nome": "Victor"},
]

print("Nomes encontrados:", extrair_nomes(pessoas))
