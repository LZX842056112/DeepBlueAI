import numpy as np


def exam(arr):
    return arr+100


res = exam(np.random.randint(1, 10, size=(2, 3)))

print(res)
