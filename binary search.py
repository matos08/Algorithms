def pesquisa_binaria(lista, item):
    """
    A pesquisa binária é um algoritmo eficiente para encontrar um item em uma lista ordenada,
    reduzindo pela metade o espaço de busca a cada iteração, levando a uma complexidade de tempo
    'O(log n)'.
    """
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))  # => 1
print(pesquisa_binaria(minha_lista, -1))  # => None
