# Exercise 3: E-Commerse order Processing

import random
import sys
import time
import tracemalloc

LAST_NAME = "APON"
STUDENT_ID = "TUPM-26-1876"
FAVORITE_ARTIST = "TEETEEPOR"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(ord(c) - 96 for c in FAVORITE_ARTIST.lower () if c.isalpha())

def time_growth(c1, c2):
    if c2 == c1:
        return "0(1)"
    if c2 - c1 <= 2:
        return "0(log n)"
    return "0(n)" if c2 / c1 < 2.5 else "0(n²)"

def peak_memory(func, *args):
    tracemalloc.start()
    func(*args)
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return peak

def space_growth(m1, m2):
    return "0(1)" if m2 <= 1.5 * m1 + 256 else "0(n)"

def bubble_sort(data):
    a, comparisons, swaps = data.copy(), 0, 0
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, swaps

def selection_sort(data):
    a, comparisons, swaps = data.copy(), 0, 0
    for i in range(len(a) - 1):
        minimum = i
        for j in range(i + 1, len(a)):
            comparisons += 1
            if a[j] < a[minimum]:
                minimum = j
        if minimum != i:
            a[i], a[minimum] = a[minimum], a[i]
            swaps += 1
    return a, comparisons, swaps

def insertion_sort(data):
    a, comparisons, shifts = data.copy(), 0, 0
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0:
            comparisons += 1
            if a[j] <= key:
                break
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return a, comparisons, shifts

def measure(sort_function, data, trials=5):
    times = []
    for _ in range(trials):
        start = time.perf_counter()
        result = sort_function(data)
        times.append(time.perf_counter() - start)
    return result, sum(times) / trials

orders = [(ID_SUM* 7 + i * ARTIST_SUM) % 1000 for i in range(100)]

random.seed(SEED_DIGIT)
shuffled = orders.copy()
random.shuffle(shuffled)

conditions = {
    "Sorted": sorted(orders),
    "Reverse": sorted(orders, reverse=True),
    "Random": shuffled,
}

algorithms =[
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
]

records = []
for cond, d in conditions.items():
    for name, func in algorithms:
        result, avg_time = measure(func, d)
        records.append((cond, name, result[1], result[2], avg_time, result[0] == sorted(orders)))

complexity = []
for name, func in algorithms:
    worst = [func(list(range(n, 0, -1))) [1] for n in (100, 200)]
    best = [func(list(range(n, 0, + 1))) [1] for n in (100, 200)]
    d1, d2 = list(range(100, 0, -1)), list(range(200, 0, -1))
    m1 = peak_memory(func, d1) - sys.getsizeof(d1)
    m2 = peak_memory(func, d2) - sys.getsizeof(d2)
    complexity.append((name, time_growth (*best),  time_growth (*worst), space_growth(max(m1, 0), max(m2, 0))))

print("EXERSICE 3: E-COMMERCE ORDER PROCESSING")
print("Generated Order dataset (first 10 of", len(orders),"):", orders[:10])
print("Sorted Input (first 10 of:", conditions["Sorted"][:10])
print("Reverse Input (first 10 of:", conditions["Reverse"][:10])
print("Random Input (first 10 of:", conditions["Random"][:10])
print()
print(f"{'Conditions':<10}{'Algoritm':<16}{'Comparisons':>12}{'Movements':>11}{'Time (s)':>13}{'Sorted':>8}")
for cond, name, c, m, t, ok, in records:
    print(f"{cond:<10}{name:<16}{c:>12}{m:>11}{t::>13.8f}{str(ok):>8}")
print()
print("Big O Analysis and Best-, Average-, Worst-Case Observations")
print(f"{'Algorithm':<16}{'Best (Sorted)':<16}{'Worst (Reverse)':<18}{'Space'}")
for name, best, worst, space, in complexity:
    print(f"{name:<16}{best:<16}{worst:<18}{space}")
print()
print("Final Output:")
print("All sorting results verified:", all(r[5] for r in records))     