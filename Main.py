import multiprocessing
import time
import random
import matplotlib.pyplot as plt

# Define una función para la búsqueda secuencial
def busqueda_secuencial(arr, elemento):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == elemento:
            end_time = time.time()
            return end_time - start_time
    end_time = time.time()
    return end_time - start_time

# Define una función para la búsqueda binaria
def busqueda_binaria(arr, elemento):
    start_time = time.time()
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == elemento:
            end_time = time.time()
            return end_time - start_time
        elif arr[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    end_time = time.time()
    return end_time - start_time

# Define una función para el algoritmo de ordenamiento de la burbuja
def ordenamiento_burbuja(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end_time = time.time()
    return end_time - start_time

# Define una función para el algoritmo Quick Sort
def quick_sort(arr):
    def _quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quick_sort(arr, low, pivot_index)
            _quick_sort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high
        done = False
        while not done:
            while left <= right and arr[left] <= pivot:
                left = left + 1
            while arr[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                done= True
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[low], arr[right] = arr[right], arr[low]
        return right

    start_time = time.time()
    _quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    # Crea un arreglo de ejemplo
    mi_arreglo = random.sample(range(1, 10001), 1000)  # Arreglo desordenado de 1000 elementos
    elemento_a_buscar = random.choice(mi_arreglo)  # Elemento aleatorio a buscar

    # Crear un pool de procesos
    pool = multiprocessing.Pool(processes=len([busqueda_secuencial, busqueda_binaria, ordenamiento_burbuja, quick_sort]))
    resultados = pool.starmap(busqueda_secuencial, [(mi_arreglo, elemento_a_buscar), (mi_arreglo, elemento_a_buscar), (mi_arreglo.copy(), None), (mi_arreglo.copy(), None)])

    # Almacena los tiempos de ejecución en una lista
    nombres_algoritmos = ["Búsqueda Secuencial", "Búsqueda Binaria", "Ordenamiento de Burbuja", "Quick Sort"]
    tiempos_ejecucion = resultados

    # Encuentra el algoritmo más rápido
    algoritmo_mas_rapido = nombres_algoritmos[tiempos_ejecucion.index(min(tiempos_ejecucion))]

    # Crea un gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(nombres_algoritmos, tiempos_ejecucion, color='skyblue')
    plt.xlabel('Algoritmo')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Tiempo de Ejecución de Algoritmos')
    plt.xticks(rotation=45, ha='right')

    # Muestra el gráfico
    plt.tight_layout()
    plt.show()

    # Imprime el algoritmo más rápido
    print(f"El algoritmo más rápido fue: {algoritmo_mas_rapido}")
