# Exercise 2: University Enrollment

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

def build_AB(k):
    A = [ID_SUM + i * SEED_DIGIT for i in range(k)]
    B = [ARTIST_LENGTH * 3 + i * NAME_LENGTH for i in range(k)]
    return A, B

def merge(a,b):
    i = j = comparisons = 0
    result = []
    while i < len(a) and j < len(b):
        comparisons += 1
        if a[i]<= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[i])
            j += 1
    result += a[i:]
    result += b[j:]
    return result, comparisons

A, B = build_AB(10)
merged, comparisons = merge(A, B)
ordered = merged == sorted(A + B)

A1, B1 = build_AB(1000)
A2, B2 = build_AB(2000)
c1 = merge(A1, B1)[1]
c2 = merge(A2, B2)[1]
m1 = peak_memory(merge, A1, B1)
m2 = peak_memory(merge, A2, B2)
time_class = "0(n + m)" if time_growth(c1, c2) == "0(n)" else time_growth(c1, c2)
space_class = "0(n + m)" if space_growth (m1, m2) == "0(n)" else space_growth(m1, m2)

print("EXERCISE 2: UNIVERSITY ENROLLMENT RECORDS")
print("Department A:", A)
print("Department B:", B)
print("Consolidated Dataset:", merged)
print()
print("Records Before Consolidation:", len(A) + len(B))
print("Records After Consolidation:", len(merged))
print("Comparison Count:", comparisons)
print("Ordering verification:", ordered)
print()
print("Time and Space Complexity")
print(f"Merge: Time {time_class}, Space {space_class}")
print()
print("Final Output")
print(f"{len(A)} + {len(B)} records merged into {len(merged)} ordered records using {comparisons} comparisons")