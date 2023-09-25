import random
import timeit
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

def merge(arr, left, middle, right):
    left_copy = arr[left:middle + 1]
    right_copy = arr[middle + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1

    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1

    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)

def generate_data_sizes(start, stop, step):
    return list(range(start, stop + 1, step))

def measure_insertion_sort_time(data_size):
    data = [random.randint(0, 1000) for _ in range(data_size)]
    timer = timeit.Timer(lambda: insertion_sort(data.copy()))
    return timer.timeit(number=1000)  # Ejecutar 1000 veces para medir el tiempo

def measure_merge_sort_time(data_size):
    data = [random.randint(0, 1000) for _ in range(data_size)]
    timer = timeit.Timer(lambda: merge_sort(data.copy(), 0, len(data) - 1))
    return timer.timeit(number=1000)  # Ejecutar 1000 veces para medir el tiempo

def main():
    min_data_size = 2
    max_data_size = 128
    step_size = 2

    data_sizes = generate_data_sizes(min_data_size, max_data_size, step_size)
    insertion_sort_times = []
    merge_sort_times = []

    for size in data_sizes:
        insertion_time = measure_insertion_sort_time(size)
        merge_time = measure_merge_sort_time(size)
        insertion_sort_times.append(insertion_time)
        merge_sort_times.append(merge_time)

    plt.plot(data_sizes, insertion_sort_times, label="Insertion Sort")
    plt.plot(data_sizes, merge_sort_times, label="Merge Sort")
    plt.xlabel("Tamaño de datos")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.title("Eficiencia de Insertion Sort vs. Merge Sort")
    plt.grid(True)
    plt.savefig("grafico.png")


main()
