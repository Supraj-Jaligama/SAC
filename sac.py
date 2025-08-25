import numpy as np
import pandas as pd 

data = [2,3,4,5,6,7,8,9,10]

s = pd.Series(data)

print("Mean:", s.mean())
print("median:", s.median())
print("Standard Deviation:", s.std())
print("variance:", s.var())
print("Min:", s.min(),"Max:", s.max())
print("quatiles:", s.quantile())
