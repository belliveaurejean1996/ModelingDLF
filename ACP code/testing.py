import numpy as np

Array = [[False, True, False], [False, True, False]]


Count = np.count_nonzero(Array, axis=0)
w = np.where(Array == True)

print(Count[1])