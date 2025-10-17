def binary_search(lista, item):
    """
    Realiza uma busca binária em uma lista ordenada.
    Este algoritmo funciona dividindo repetidamente pela metade a porção da lista
    que poderia conter o item, até reduzir as localizações possíveis a apenas uma.
    Para funcionar, a lista precisa estar ordenada. A complexidade é O(log n)
    porque a cada passo, o tamanho do problema é reduzido pela metade.

    # Complexidade: O(log n)
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

# Teste de uso
lista_teste = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
item_procurado = 7
posicao = binary_search(lista_teste, item_procurado)

print(f"A lista ordenada é: {lista_teste}")
if posicao is not None:
    print(f"O item {item_procurado} foi encontrado na posição: {posicao}")
else:
    print(f"O item {item_procurado} não foi encontrado na lista.")
