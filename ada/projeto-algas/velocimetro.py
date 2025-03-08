import random
from memory_profiler import memory_usage
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(5000)

def process_data(arr, i):
    if i * 1.2 < len(arr):
        random.shuffle(arr)
        if arr == sorted(arr):
            return 1
        else:
            return process_data(arr, i + 1)
    return 0


def declare_arr(size):
    arr = list(range(size))
    random.shuffle(arr)
    return arr


def minha_funcao(size):
    inicio = time.time()
    process_data(declare_arr(size), 0)
    fim = time.time()
    tempo_processamento = fim - inicio
    return tempo_processamento


def get_results(sizes):
    memory_result = []
    time_result = []

    for size in sizes:
        print(f"Testing with size = {size}")

        mem_usage, process_time = memory_usage(
            (minha_funcao, (size,), {}),
            max_usage=True, retval=True
        )

        memory_result.append(mem_usage)
        time_result.append(process_time)
        print(f"Memory usage: {mem_usage} MiB")
        print(f"Execution time: {process_time} seconds")
        print()

    return memory_result, time_result

def plot_results(sizes, memory_result, time_result):
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('Valor Somado')
    ax1.set_ylabel('Memória Usada (MiB)', color=color)
    ax1.plot(sizes, memory_result, 'o-', color=color, label='Memoria Usada')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Tempo de execução (segundos)', color=color)
    ax2.plot(sizes, time_result, 's-', color=color, label='Tempo de execução')
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()
    plt.title('Memória Usada e Tempo de execução vs Valor Somado')
    plt.show()

if __name__ == "__main__":
    sizes = list(range(1000, 6000, 100))
    memory_result, time_result = get_results(sizes)
    plot_results(sizes, memory_result, time_result)