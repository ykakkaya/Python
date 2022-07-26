import pandas as pd
import numpy as np

#farklı veri tiplerini içerisinde barındırabilir.np arraylar tek veri tipinde olmalıydı.
numbers=[10,20,30,40,51]

pandas_series1=pd.Series(numbers)
print(pandas_series1)

letters=["a","b","c","d","e"]
pandas_series2=pd.Series(letters)
print(pandas_series2)

#pandas serilerinin key (index) lerini biz yollayabiliriz.
pandas_series=pd.Series(numbers,letters)
print(pandas_series)


np_array=np.random.randint(20,50,8)
pd_series=pd.Series(np_array)
print(pd_series)


print(pandas_series)
#pandas series elemanlara ulaşma
print(pandas_series[0])
print(pandas_series[:3])
print(pandas_series["c"])
print(pandas_series[["a","d"]])

#numpy metodlarıda kullanılabilir

print(pandas_series.dtype)
print(pandas_series.sum())
print(pandas_series.shape)
print(pandas_series.ndim)
print(pandas_series.max())
print(pandas_series.argmax())
print(pandas_series.min())
print(pandas_series.argmin())

#aritmetik işlemler

print(pandas_series+pandas_series)
print(pandas_series+50)
print(np.sqrt(pandas_series))
res=(pandas_series>=30)&(pandas_series %2==0)
print(pandas_series[res])