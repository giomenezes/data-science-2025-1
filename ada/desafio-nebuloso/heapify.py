def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def heapify(a, n, i):
    """
    Função para manter a propriedade de heap em um array.
    a - array, n - número de elementos, i - posição do elemento que deve ser colocado em propriedade de heap
    """
    e = left(i)
    d = right(i)
    max = i

    if e < n and a[e] > a[max]:
        max = e
    if d < n and a[d] > a[max]:
        max = d

    if max != i:
        a[i], a[max] = a[max], a[i]  # Troca os elementos
        heapify(a, n, max)

def build_heap(a, n):
    """
    Função para construir um heap a partir de um array.
    a - array, n - número de elementos
    """
    for i in range((n - 1) // 2, -1, -1):
        heapify(a, n, i)
        print("Array:", a)

# Exemplo de uso
if __name__ == "__main__":
    arr = [2, 5, 8 ,13, 21, 1, 3, 34]
    n = len(arr)
    print("Array original:", arr)

    build_heap(arr, n)
    print("Array após buildHeap:", arr)