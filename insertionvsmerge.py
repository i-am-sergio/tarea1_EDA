import timeit, random

def InsertionSort(array):
    for i in range(1,len(array)):
        current = array[i]
        j = i - 1
        while j>=0 and array[j]>current:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current

def merge(my_array, inicio, medio, fin):
    size_izq = medio - inicio + 1
    size_der = fin - medio
    sub_array_izq = my_array[inicio:inicio + size_izq]
    sub_array_der = my_array[medio + 1:medio + 1 + size_der]

    i = 0
    j = 0
    k = inicio

    while i < size_izq and j < size_der:
        if sub_array_izq[i] <= sub_array_der[j]:
            my_array[k] = sub_array_izq[i]
            i += 1
        else:
            my_array[k] = sub_array_der[j]
            j += 1
        k += 1

    while i < size_izq:
        my_array[k] = sub_array_izq[i]
        i += 1
        k += 1

    while j < size_der:
        my_array[k] = sub_array_der[j]
        j += 1
        k += 1


def MergeSort(my_array, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2
        MergeSort(my_array, inicio, medio)
        MergeSort(my_array, medio + 1, fin)
        merge(my_array, inicio, medio, fin)


def CallInsertionSort():
    A = [3, 1, 2, 5, 4]
    InsertionSort(A)
    # print(A)

def CallMergeSort():
    B = [3, 1, 2, 5, 4]
    MergeSort(B, 0, len(B)-1)
    # print(B)

def ComplejidadMejorCaso():
    print("COMPLEJIDAD MEJOR CASO")
    insertion_sort_time = timeit.timeit(CallInsertionSort, number=1000)
    merge_sort_time = timeit.timeit(CallMergeSort, number=1000)
    print(f"Tiempo de ejecución de Insertion Sort: {insertion_sort_time} segundos")
    print(f"Tiempo de ejecución de Merge Sort: {merge_sort_time} segundos")
    

big_array = [random.randint(1, 1000000) for _ in range(10000)] # size = 10000

def CallInsertionSort2():
    A = big_array.copy()
    InsertionSort(A)
    # print(A)

def CallMergeSort2():
    B = big_array.copy()
    MergeSort(B, 0, len(B)-1)

def ComplejidadPeorCaso():
    print("COMPLEJIDAD PEOR CASO")
    insertion_sort_time = timeit.timeit(CallInsertionSort2, number=1)
    merge_sort_time = timeit.timeit(CallMergeSort2, number=1)
    print(f"Tiempo de ejecución de Insertion Sort: {insertion_sort_time} segundos")
    print(f"Tiempo de ejecución de Merge Sort: {merge_sort_time} segundos")


ComplejidadMejorCaso()
ComplejidadPeorCaso()
