import pickle
import numpy as np
import pandas as pd
from numpy import argmin

data_set = pd.read_csv('data_s1_t1.csv').values.astype('float32')

bound_low = np.min(data_set, axis=0)
bound_high = np.max(data_set, axis=0)
print(bound_low)
print(bound_high)

with open('bound_low.txt', 'wb') as handle:
    pickle.dump(bound_low, handle)
with open('bound_high.txt', 'wb') as handle:
    pickle.dump(bound_high, handle)

with open('bound_low.txt','rb') as handle:
	bound_low1 = pickle.load(handle)

with open('bound_high.txt','rb') as handle:
	bound_high1 = pickle.load(handle)

print(bound_low1)
print(type(bound_low1))
print(bound_high1)
print(type(bound_high1))
input_data = np.random.normal(loc=0, scale=1.0, size = 15)
print(input_data)
print(input_data.shape)
for i in range(0, input_data.shape[0]):
        if input_data[i]>bound_high[i]:
            input_data[i] = bound_high[i]
        if input_data[i]<bound_low[i]:
            input_data[i] = bound_low[i]

print(input_data)
print(input_data.shape)