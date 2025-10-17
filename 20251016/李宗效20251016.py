import time


def fibnacci(n):
    if n <= 1: return n
    return fibnacci(n - 1) + fibnacci(n - 2)


start = time.perf_counter()
for i in range(1000000):
    fibnacci(20)
end = time.perf_counter()
print((end - start)) # 1464.381099
