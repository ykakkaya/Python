import numpy as np


#python listesi aldık
list=[1,2,3,4,5,6,7,8,9]

#listeyi numpy array a çevirdik
np_array=np.array(list)

print(type(list))
print(type(np_array))

#numpy array den de yine 3 e 3 lük bir matrise dönüştürdük
print(f"numpy array = {np_array}")
np_multi=np_array.reshape(3,3)
print(f"numpy matris =\n {np_multi}")

#elimizdeki numpy array larin boyutunu yazdırdık.
print(f"numpy array boyutu = {np_array.shape}")
print(f"numpy matris boyutu = {np_multi.shape}")