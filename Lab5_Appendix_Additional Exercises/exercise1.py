# Exercise 1: Emergency Dsoatch Record Search

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

def build_original(n):
    return [ID_SUM * 10 + i * SEED_DIGIT for i in range(n)]

def build_rotated(n):
    original = build_original(n)
    return original[SEED_DIGIT:] + original[:SEED_DIGIT]

def rotated_search(a, t):
    low, high, comparisons = 0, len(a) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if a[mid] == t:
            return mid, comparisons
        if a[low] <= a[mid]:
            if a[low] <= t < a[mid]:
                 high = mid - 1
            else:
                low = mid + 1
        else:
            if a[mid] < t <= a[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1, comparisons

def linear_search(a, t):
    for i, v in enumerate(a):
        if v == t:
            return i, i + 1
    return -1, len(a)

n = 20
original = build_original(n)
rotated = build_rotated(n)
target = original[(ID_SUM + ARTIST_SUM) % n]

bi, bc = rotated_search(rotated, target)
li, lc = linear_search(rotated, target)

r1, r2 = build_rotated(1000), build_rotated(2000)
complexity = {}
for name, f in [("Rotated Binary Search", rotated_search), ("Linear Search", linear_search)]:
    c1 = f(r1, -1)[1]
    c2 = f(r2, -1)[1]
    m1 = peak_memory(f, r1, -1)
    m2 = peak_memory(f, r2, -1)
    complexity[name] = (time_growth(c1, c2), space_growth(m1, m2))

print("EXERCISE 1: EMERGENCY DISPATCH RECORD SEARCH")
print("Original:", original)
print("Rotated:", rotated)
print("Target Incident:", target)
print()
if bi == -1:
    print("Rotated Binary Search: not found")
else:
    print(f"Rotated Binary Search: found at index {bi}")
print("Comparison counts:", bc)
print()
print(f"Linear -> index={li}, comparisons={lc}")
print("Comparison Reduction:", lc - bc)
print()
print("Time and Space complexity")
for name, (t, s) in complexity.items():
    print(f"{name}: Time {t}, Space {s}")
print()
print("Final Output:")
print(f"Target {target} located at index {bi} using {bc} comparisons (Linear Search: {lc})")