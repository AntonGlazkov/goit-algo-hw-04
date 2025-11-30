import random
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def generate_data(size, case):
    arr = [random.randint(0, size) for _ in range(size)]
    if case == "sorted":
        arr.sort()
    elif case == "reversed":
        arr.sort(reverse=True)
    return arr


def measure_sort(sort_func, data, number=5):
    def run():
        arr = data.copy()
        sort_func(arr)

    return timeit.timeit(run, number=number)


def main():
    sizes = [1000, 5000, 10000]
    cases = ["random", "sorted", "reversed"]

    for size in sizes:
        print(f"\nРозмір масиву: {size}")
        for case in cases:
            data = generate_data(size, case)
            print(f"  Випадок даних: {case}")

            t_insertion = measure_sort(insertion_sort, data)
            print(f"    insertion_sort: {t_insertion:.6f} c")

            def merge_sort_wrapper(a):
                merge_sort(a)

            t_merge = measure_sort(merge_sort_wrapper, data)
            print(f"    merge_sort:     {t_merge:.6f} c")

            t_timsort = measure_sort(sorted, data)
            print(f"    Timsort(sorted): {t_timsort:.6f} c")


if __name__ == "__main__":
    main()
