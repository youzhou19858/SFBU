import time
import sys

sys.setrecursionlimit(10**6)

def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

n = 20
# Benchmark for n = 20
start = time.time()
print(fib_recursive(n))
end = time.time()
print(f"Recursive time for n = {n}: ", end - start)

start = time.time()
print(fib_iterative(n))
end = time.time()
print(f"Iterative time for n = {n}: ", end - start)

n = 1000
# Benchmark for n = 100000
start = time.time()
print(fib_iterative(n))
end = time.time()
print(f"Iterative time for n = {n}: ", end - start)

# Commenting this out because it's infeasible
start = time.time()
print(fib_recursive(n))
end = time.time()
print(f"Recursive time for n = {n}: ", end - start)