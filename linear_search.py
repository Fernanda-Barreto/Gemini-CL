def encontrar_maximo(lista):
    """
    Encontra o valor máximo em uma lista.
    Este algoritmo percorre a lista uma vez, comparando cada elemento
    com o máximo encontrado até agora. A complexidade é O(n) porque
    o número de operações cresce linearmente com o tamanho da lista.

    # Complexidade: O(n)
    """
    if not lista:
        return None
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

# Teste de uso
lista_teste = [3, 1, 4, 1, 5, 9, 2, 6]
max_valor = encontrar_maximo(lista_teste)
print(f"A lista é: {lista_teste}")
print(f"O valor máximo na lista é: {max_valor}")
