def get_parent(child):
    """
    Retorna o índice do pai de um dado índice filho em um heap.
    """
    if child % 2 == 0:
        return (child - 2) // 2
    else:
        return (child - 1) // 2


def swap(arr, i, j):
    """
    Troca os elementos nos índices i e j no array.
    """
    arr[i], arr[j] = arr[j], arr[i]


def insert_into_heap(heap_size, arr):
    """
    Insere um elemento no heap e mantém a propriedade do heap.
    """
    child = heap_size
    parent = get_parent(child)

    while child > 0 and parent >= 0 and arr[parent] < arr[child]:
        swap(arr, parent, child)
        child = parent
        parent = get_parent(child)


def adjust_heap(heap_size, arr):
    """
    Ajusta o heap para manter a propriedade do heap após remover a raiz.
    """
    parent = 0
    while True:
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2
        largest = parent

        if left_child <= heap_size and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child <= heap_size and arr[right_child] > arr[largest]:
            largest = right_child

        if largest == parent:
            break

        swap(arr, parent, largest)
        parent = largest


def heap_sort(arr):
    """
    Ordena um array usando o algoritmo Heap Sort.
    """
    print("Vetor original:", arr)

    # Constrói o heap
    for heap_size in range(len(arr) - 1):
        insert_into_heap(heap_size, arr)

    # Extrai elementos do heap
    for heap_size in range(len(arr) - 1, 0, -1):
        swap(arr, 0, heap_size)
        print(f"Depois da troca do índice {heap_size}:", arr)
        adjust_heap(heap_size - 1, arr)


if __name__ == "__main__":
    arr = [16, 13, 5, 6, 12, 9, 7, 4, 11, 8, 10, 14, 15]
    heap_sort(arr)