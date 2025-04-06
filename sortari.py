import time
import random

# --- Counting Sort (pentru Radix sort baza 10) ---
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort_base10(arr):
    if not arr:
        return
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# --- Radix Sort baza 2^16 ---
def radix_sort_base2_16(arr):
    if not arr:
        return
    base = 1 << 16
    max_val = max(arr)
    shift = 0
    while max_val >> shift > 0:
        count = [0] * base
        output = [0] * len(arr)

        for num in arr:
            count[(num >> shift) & (base - 1)] += 1

        for i in range(1, base):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            index = (arr[i] >> shift) & (base - 1)
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        for i in range(len(arr)):
            arr[i] = output[i]
        shift += 16

# --- Merge Sort ---
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        result.append(left[i] if left[i] < right[j] else right[j])
        if left[i] < right[j]:
            i += 1
        else:
            j += 1
    return result + left[i:] + right[j:]

# --- Shell Sort ---
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# --- Quick Sort (cu pivot mediana din 3) ---
def median_of_three(arr, a, b, c):
    values = [(arr[a], a), (arr[b], b), (arr[c], c)]
    values.sort()
    return values[1][1]

def partition(arr, low, high):
    mid = low + (high - low) // 2
    pivot_index = median_of_three(arr, low, mid, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort_util(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_util(arr, low, pi - 1)
        quick_sort_util(arr, pi + 1, high)

def quick_sort(arr):
    quick_sort_util(arr, 0, len(arr) - 1)

# --- Heap Sort ---
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# --- Bucket Sort (pe float între 0 și 1) ---
def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        idx = int(n * num)
        buckets[idx].append(num)
    for bucket in buckets:
        bucket.sort()
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result

# --- Testare și măsurare timp ---
def test_sort(sort_func, arr, inplace=True):
    copy = arr[:] if inplace else arr
    start = time.time()
    if inplace:
        sort_func(copy)
    else:
        copy = sort_func(copy)
    end = time.time()
    assert copy == sorted(copy), f"Sortare greșită cu {sort_func.__name__}"
    return end - start

# --- Generatoare de date aleatoare ---
def generate_random_integers(N, Max):
    return [random.randint(0, Max) for _ in range(N)]

def generate_random_floats(N):
    return [random.random() for _ in range(N)]
def run(name, func, arr, fout, inplace=True):
    try:
        data = arr[:] if inplace else arr
        start = time.time()

        if inplace:
            func(data)
        else:
            data = func(data)

        end = time.time()
        duration = round(end - start, 5)

        if data != sorted(arr):
            print(f"[Eroare] {name} NU a sortat corect!")
            fout.write(f"[Eroare] {name} NU a sortat corect!\n")
        else:
            print(f"{name}: {duration} sec")
            fout.write(f"{name}: {duration} sec\n")

    except Exception as e:
        print(f"[Exceptie] {name} a eșuat: {e}")
        fout.write(f"[Exceptie] {name} a eșuat: {e}\n")

def main():
    with open("tests.in", "r") as fin, open("results.txt", "w") as fout:
        T = int(fin.readline())
        tests = [tuple(map(int, fin.readline().split())) for _ in range(T)]

        for t, (N, Max) in enumerate(tests, 1):
            print(f"\n=== Test {t}: N = {N}, Max = {Max} ===")
            fout.write(f"\n=== Test {t}: N = {N}, Max = {Max} ===\n")

            original = generate_random_integers(N, Max)

            run("RadixSort Base10", radix_sort_base10, original, fout, inplace=True)
            run("RadixSort Base2^16", radix_sort_base2_16, original, fout, inplace=True)
            run("MergeSort", merge_sort, original, fout, inplace=False)
            run("ShellSort", shell_sort, original, fout, inplace=True)
            run("QuickSort", quick_sort, original, fout, inplace=True)
            run("HeapSort", heap_sort, original, fout, inplace=True)
            
            if N <= 100000:
                 try:
                    floats = generate_random_floats(N)
                    start = time.time()
                    sorted_floats = bucket_sort(floats)
                    end = time.time()
                    assert sorted_floats == sorted(floats)
                    duration = round(end - start, 5)
                    print(f"BucketSort: {duration} sec")
                    fout.write(f"BucketSort: {duration} sec\n")
                 except Exception as e:
                    print(f"[Exceptie] BucketSort a eșuat: {e}")
                    fout.write(f"[Exceptie] BucketSort a eșuat: {e}\n")

                 try:
                    start = time.time()
                    native_sorted = sorted(original)
                    end = time.time()
                    assert native_sorted == sorted(original)
                    duration = round(end - start, 5)
                    print(f"Native sorted(): {duration} sec")
                    fout.write(f"Native sorted(): {duration} sec\n")
                 except Exception as e:
                    print(f"[Exceptie] Native sorted() a eșuat: {e}")
                    fout.write(f"[Exceptie] Native sorted() a eșuat: {e}\n")

if __name__ == "__main__":
    main()