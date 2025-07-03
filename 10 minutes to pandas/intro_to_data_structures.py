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

# From dict

d = {"b": 1, "a": 0, "c": 2}
dfd = pd.Series(d)
dfd = pd.Series(d, index=["b", "c", "d", "a"]) # adding a new index will show result as NaN, a std data marker for missing data

print(dfd)
