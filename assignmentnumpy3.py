import numpy as np


lst = [1, 2, 0, 0, 4, 0]

arr = np.array(lst)

indices = np.nonzero(arr)

print(indices)
