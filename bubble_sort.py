def bubble_sort(lista):
    """
    Ordena uma lista usando o algoritmo Bubble Sort.
    Este algoritmo compara repetidamente pares de elementos adjacentes e os troca
    se estiverem na ordem errada. O processo é repetido até que a lista esteja
    ordenada. A complexidade é O(n^2) devido aos dois loops aninhados.

    # Complexidade: O(n^2)
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Teste de uso
lista_teste = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_teste}")
bubble_sort(lista_teste)
print(f"Lista ordenada: {lista_teste}")
