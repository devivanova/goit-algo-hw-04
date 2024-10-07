import random
import timeit


# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Тестові масиви
small_array = random.sample(range(100), 10)  # маленький масив
medium_array = random.sample(range(10000), 1000)  # середній масив
large_array = random.sample(range(100000), 10000)  # великий масив


# Використання timeit для вимірювання часу виконання
def test_sorting_algorithms():
    print("Час для маленького масиву (10 елементів):")
    print("Merge Sort:", timeit.timeit(
        lambda: merge_sort(small_array[:]), number=1000))
    print("Insertion Sort:", timeit.timeit(
        lambda: insertion_sort(small_array[:]), number=1000))
    print("Timsort (sorted):", timeit.timeit(
        lambda: sorted(small_array[:]), number=1000))

    print("\nЧас для середнього масиву (1000 елементів):")
    print("Merge Sort:", timeit.timeit(
        lambda: merge_sort(medium_array[:]), number=100))
    print("Insertion Sort:", timeit.timeit(
        lambda: insertion_sort(medium_array[:]), number=100))
    print("Timsort (sorted):", timeit.timeit(
        lambda: sorted(medium_array[:]), number=100))

    print("\nЧас для великого масиву (10000 елементів):")
    print("Merge Sort:", timeit.timeit(
        lambda: merge_sort(large_array[:]), number=10))
    print("Insertion Sort:", timeit.timeit(
        lambda: insertion_sort(large_array[:]), number=10))
    print("Timsort (sorted):", timeit.timeit(
        lambda: sorted(large_array[:]), number=10))


test_sorting_algorithms()
