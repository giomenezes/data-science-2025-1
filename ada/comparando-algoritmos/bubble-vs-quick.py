import copy
import random
from memory_profiler import memory_usage # type: ignore
import time
import pandas as pd # type: ignore

def sum_of_n_init(n):
    acumul_acelerate = 0
    for i in range(1, n+1):
        acumul_acelerate = acumul_acelerate + i
    return acumul_acelerate

def declare_arr(size):
    arr = [sum_of_n_init(i + 1) for i in range(size)]
    random.shuffle(arr)
    return arr

def partition(arr, low, high):
    # Pega o último elemento como pivô
    pivot = arr[high]
    
    # Índice do menor elemento
    i = low - 1
    
    for j in range(low, high):
        # Se o elemento atual for menor ou igual ao pivô
        if arr[j] <= pivot:
            # Incrementa o índice do menor elemento
            i += 1
            # Troca arr[i] com arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Troca arr[i+1] com arr[high] (o pivô)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high, counter):
    if low < high:
        counter[0] += 1
        # Encontra o índice do pivô
        pi = partition(arr, low, high)
        
        # Divide e conquista
        quick_sort(arr, low, pi-1, counter)
        quick_sort(arr, pi+1, high, counter)

def bubble_sort(arr):
    n = len(arr)
    cycles = 0
    
    # Percorre todos os elementos do array
    for i in range(n):
        # Últimos i elementos já estão no lugar certo, então não precisamos mais verificar eles
        for j in range(0, n-i-1):
            cycles += 1
            # Percorre o array de 0 a n-i-1
            # Troca se o elemento atual for maior que o próximo
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return cycles

def minha_funcao(arr, sort_type):
    arr_copy = copy.deepcopy(arr)
    
    if (sort_type == 'bubble'):
        inicio = time.time()  # Captura o tempo de início
        cycles = bubble_sort(arr_copy)
    else:
        inicio = time.time()  # Captura o tempo de início
        counter = [0]
        quick_sort(arr_copy, 0, len(arr_copy)-1, counter)
        cycles = counter[0]
    
    time.sleep(0.1)
    fim = time.time()  # Captura o tempo de fim
    tempo_processamento = fim - inicio  # Calcula o tempo de processamento em segundos
    return tempo_processamento, cycles

def get_results(arr, sort_type):
    mem_usage, (process_time, cycles) = memory_usage(
        (minha_funcao, (arr, sort_type), {}), max_usage=True, retval=True
    )
    return mem_usage, process_time, cycles

if __name__ == "__main__":
    df = pd.DataFrame(columns=['arr_length', 'sort', 'memory_spent', 'process_time', 'cycles'])
    for size in [10, 100, 1000, 10000, 100000]:
        arr = declare_arr(size)
        for sort_type in ['bubble', 'quick']:
            memory_spent, process_time, cycles = get_results(arr[:], sort_type)
            df = pd.concat([df, pd.DataFrame({
                'arr_length': [size],
                'sort': [sort_type],
                'memory_spent': [memory_spent],
                'process_time': [round(process_time, 10)],
                'cycles': [cycles]
            })], ignore_index=True)
    df.to_csv("dados.csv", index=False)