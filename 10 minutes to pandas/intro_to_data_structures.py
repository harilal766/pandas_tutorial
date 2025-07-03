import numpy as np
import pandas as pd

"""
https://pandas.pydata.org/docs/user_guide/dsintro.html#dsintro
"""
# Series

limit = 5
data = list(range(1, limit+1))
index = ["a", "b","c","d","e"]

s = pd.Series(data,index=index)

ser = pd.Series(np.random.randn(limit))

print(ser)